from app import app, db, Product, Promotion

def init_db():
    with app.app_context():
        db.create_all()

        products = [
            Product(name='Jeruk', category='Minuman', variant='Dingin', price=12000),
            Product(name='Jeruk', category='Minuman', variant='Panas', price=10000),
            Product(name='Teh', category='Minuman', variant='Manis', price=8000),
            Product(name='Teh', category='Minuman', variant='Tawar', price=5000),
            Product(name='Kopi', category='Minuman', variant='Dingin', price=8000),
            Product(name='Kopi', category='Minuman', variant='Panas', price=6000),
            Product(name='Mie', category='Makanan', variant='Goreng', price=15000),
            Product(name='Mie', category='Makanan', variant='Kuah', price=15000),
            Product(name='Nasi Goreng', category='Makanan', price=15000)
        ]
        db.session.bulk_save_objects(products)

        promotions = [
            Promotion(name='Nasi Goreng + Jeruk Dingin', details='Nasi Goreng + Jeruk Dingin', price=23000)
        ]
        db.session.bulk_save_objects(promotions)

        db.session.commit()

if __name__ == '__main__':
    init_db()
