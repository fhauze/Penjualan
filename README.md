localhost:5000/order [POST] buat order
Contoh Request untuk membuat order ,

{
  "tableNumber": "MEJA NO 1",
  "items": [
    {
      "productId": 1,
      "quantity": 1
    },
    {
      "productId": 3,
      "quantity": 1
    },
    {
      "productId": 4,
      "quantity": 2
    },
    {
      "productId": 2,
      "quantity": 1
    },
    {
      "productId": 5,
      "quantity": 1
    }
  ],
  "promotions": [
    {
      "promotionId": 1,
      "quantity": 2
    }
  ]
}
output :
{
	"orderId": 9,
	"printers": [
		"Printer Bar",
		"Printer Dapur"
	],
	"totalOrderPrice": "94000.00"
}
=================
Untuk Dapat Detail Order : localhost:5000/bill
{
	"createdAt": "Wed, 07 Aug 2024 10:23:04 GMT",
	"items": [
		{
			"product_id": 1,
			"quantity": 1,
			"total_price": 12000.0
		},
		{
			"product_id": 3,
			"quantity": 1,
			"total_price": 8000.0
		},
		{
			"product_id": 4,
			"quantity": 2,
			"total_price": 10000.0
		},
		{
			"product_id": 2,
			"quantity": 1,
			"total_price": 10000.0
		},
		{
			"product_id": 5,
			"quantity": 1,
			"total_price": 8000.0
		}
	],
	"orderId": 9,
	"promotions": [
		{
			"promotion_id": 1,
			"quantity": 2,
			"total_price": 46000.0
		}
	],
	"tableNumber": "MEJA NO 1"
}


