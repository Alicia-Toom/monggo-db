from pymongo import MongoClient

def main():
    client = MongoClient('mongodb://root:mysql@localhost:27016')
    db = client.test

    db.strunt.insert_one({
        "product_name": "diamond ring",
        "items_in_stock": 11,
        "carat": 18
    })

    products = db.products.find({})

    for product in products:
        print(product)

if __name__ == '__main__':
    main()
