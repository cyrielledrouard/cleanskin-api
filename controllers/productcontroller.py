from flask import jsonify, Blueprint, request, json
from db.productdb import select_products, select_products_by_id, delete_product_db
from services.productservice import add_product_service, replace_product_service
from flask import Response


product_app = Blueprint("products", __name__)


@product_app.route('/')
def get_products():
    records = select_products()
    if records is not None:
        return jsonify(records)
    else:
        return Response("Internal error", status=500, mimetype='application/json')


@product_app.route('/<int:id>')
def get_product_by_id(id):
    records = select_products_by_id(id)
    if records is not None:
        return jsonify(records)
    else:
        return Response("Internal error", status=500, mimetype='application/json')


@product_app.route('/', methods=['POST'])
def add_product():
    request_data = request.get_json()
    response = add_product_service(request_data)
    return response


@product_app.route('/<int:id>', methods=['PUT'])
def replace_product(id):
    request_data = request.get_json()
    response = replace_product_service(request_data, id)
    return response


@product_app.route('/<int:id>', methods=['DELETE'])
def delete_product(id):
    deleted_product = delete_product_db(id)
    if deleted_product is True:
        return Response("Product deleted from database", status=200, mimetype='application/json')
    else:
        return Response("Internal error", status=500, mimetype='application/json')
