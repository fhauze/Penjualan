from flask import Blueprint, request, jsonify
from models.Models import db, Product, Order, OrderItem, Promotion, OrderPromotion

bp = Blueprint('main', __name__)

@bp.route('/products', methods=['POST'])
def create_product():
    data = request.json
    product = Product(name=data['name'], category=data['category'], variant=data.get('variant'), price=data['price'])
    db.session.add(product)
    db.session.commit()
    return jsonify({'message': 'Product created', 'product': {'id': product.id, 'name': product.name, 'category': product.category, 'variant': product.variant, 'price': float(product.price)}}), 201

@bp.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([{'id': product.id, 'name': product.name, 'category': product.category, 'variant': product.variant, 'price': float(product.price)} for product in products])

@bp.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    product = Product.query.get_or_404(id)
    return jsonify({'id': product.id, 'name': product.name, 'category': product.category, 'variant': product.variant, 'price': float(product.price)})

@bp.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    data = request.json
    product = Product.query.get_or_404(id)
    product.name = data['name']
    product.category = data['category']
    product.variant = data.get('variant')
    product.price = data['price']
    db.session.commit()
    return jsonify({'message': 'Product updated', 'product': {'id': product.id, 'name': product.name, 'category': product.category, 'variant': product.variant, 'price': float(product.price)}})

@bp.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted'})

@bp.route('/promotions', methods=['POST'])
def create_promotion():
    data = request.json
    promotion = Promotion(name=data['name'], details=data['details'], price=data['price'])
    db.session.add(promotion)
    db.session.commit()
    return jsonify({'message': 'Promotion created', 'promotion': {'id': promotion.id, 'name': promotion.name, 'details': promotion.details, 'price': float(promotion.price)}}), 201

@bp.route('/promotions', methods=['GET'])
def get_promotions():
    promotions = Promotion.query.all()
    return jsonify([{'id': promotion.id, 'name': promotion.name, 'details': promotion.details, 'price': float(promotion.price)} for promotion in promotions])

@bp.route('/promotions/<int:id>', methods=['GET'])
def get_promotion(id):
    promotion = Promotion.query.get_or_404(id)
    return jsonify({'id': promotion.id, 'name': promotion.name, 'details': promotion.details, 'price': float(promotion.price)})

@bp.route('/promotions/<int:id>', methods=['PUT'])
def update_promotion(id):
    data = request.json
    promotion = Promotion.query.get_or_404(id)
    promotion.name = data['name']
    promotion.details = data['details']
    promotion.price = data['price']
    db.session.commit()
    return jsonify({'message': 'Promotion updated', 'promotion': {'id': promotion.id, 'name': promotion.name, 'details': promotion.details, 'price': float(promotion.price)}})

@bp.route('/promotions/<int:id>', methods=['DELETE'])
def delete_promotion(id):
    promotion = Promotion.query.get_or_404(id)
    db.session.delete(promotion)
    db.session.commit()
    return jsonify({'message': 'Promotion deleted'})

@bp.route('/order', methods=['POST'])
def create_order():
    data = request.json
    table_number = data['tableNumber']
    items = data['items']
    promotions = data.get('promotions', [])

    order = Order(table_number=table_number)
    db.session.add(order)
    db.session.commit()

    total_order_price = 0
    printers = set()

    for item in items:
        product = Product.query.get(item['productId'])
        if product:
            total_price = product.price * item['quantity']
            order_item = OrderItem(order_id=order.id, product_id=product.id, quantity=item['quantity'], total_price=total_price)
            db.session.add(order_item)
            total_order_price += total_price

            if product.category == 'Makanan':
                printers.add('Printer Dapur')
            elif product.category == 'Minuman':
                printers.add('Printer Bar')

    for promo in promotions:
        promotion = Promotion.query.get(promo['promotionId'])
        if promotion:
            total_price = promotion.price * promo['quantity']
            order_promotion = OrderPromotion(order_id=order.id, promotion_id=promotion.id, quantity=promo['quantity'], total_price=total_price)
            db.session.add(order_promotion)
            total_order_price += total_price

            printers.add('Printer Dapur')
            printers.add('Printer Bar')

    db.session.commit()

    return jsonify({
        'orderId': order.id,
        'totalOrderPrice': total_order_price,
        'printers': list(printers)
    })

@bp.route('/bill', methods=['GET'])
def get_bill():
    order_id = request.args.get('orderId')
    order = Order.query.get(order_id)
    if not order:
        return jsonify({'message': 'Order not found'}), 404

    order_items = OrderItem.query.filter_by(order_id=order.id).all()
    order_promotions = OrderPromotion.query.filter_by(order_id=order.id).all()

    bill_items = [{'product_id': item.product_id, 'quantity': item.quantity, 'total_price': float(item.total_price)} for item in order_items]
    bill_promotions = [{'promotion_id': promo.promotion_id, 'quantity': promo.quantity, 'total_price': float(promo.total_price)} for promo in order_promotions]

    return jsonify({
        'orderId': order.id,
        'tableNumber': order.table_number,
        'createdAt': order.created_at,
        'items': bill_items,
        'promotions': bill_promotions
    })
