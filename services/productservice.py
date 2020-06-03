from flask import Response, json
from db.productdb import insert_product, replace_product


def add_product_service(request_data):
    try:
        id = request_data['id']
        name = request_data['name']
        brand = request_data['brand']
        type = request_data['type']
        price = request_data['price']
    except Exception as e:
        print("The request format is not correct" + str(e))
        return Response(json.dumps("Invalid product"), status=400, mimetype='application/json')
    product_inserted = insert_product(id, name, brand, type, price)
    if product_inserted is True:
        return Response("Product added to database", status=200, mimetype='application/json')
    else:
        return Response("Internal error", status=500, mimetype='application/json')


def replace_product_service(request_data, id):
    try:
        name = request_data['name']
        brand = request_data['brand']
        type = request_data['type']
        price = request_data['price']
    except Exception as e:
        print("The request format is not correct" + str(e))
        return Response(json.dumps("Invalid product"), status=400, mimetype='application/json')
    product_replaced = replace_product(name, brand, type, price, id)
    if product_replaced is True:
        return Response("Product modified in database", status=200, mimetype='application/json')
    else:
        return Response("Internal error", status=500, mimetype='application/json')

