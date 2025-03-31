import os
from typing import Optional

from flask import Flask, jsonify
from flask_restful import Resource, reqparse, Api
from dotenv import load_dotenv
from flask_migrate import Migrate

from src.database.base import db
from src.data import parse_products
from src.database import db_actions


load_dotenv()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_URI")
db.init_app(app)
api = Api(app)
migrate = Migrate(app, db)


# with app.app_context():
#     # db.create_all()
    # parse_products.get_products()


class ProductAPI(Resource):
    def get(self, product_id: Optional[str] = None):
        if product_id:
            product = db_actions.get_product(product_id)
            responce = jsonify(product)
        else:
            products = db_actions.get_products()
            responce = jsonify(products)
             
        responce.status_code=200
        return responce
    

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("name")
        parser.add_argument("description")
        parser.add_argument("price")
        parser.add_argument("img_url")
        kwargs = parser.parse_args()
        msg = db_actions.add_product(**kwargs)
        responce = jsonify(msg)
        responce.status_code = 201
        return responce
    

    def put(self, product_id):
        parser = reqparse.RequestParser()
        parser.add_argument("name")
        parser.add_argument("description")
        parser.add_argument("price")
        parser.add_argument("img_url")
        kwargs = parser.parse_args()
        msg = db_actions.update_product(product_id, **kwargs)
        responce = jsonify(msg)
        responce.status_code = 200
        return responce
    

    def patch(self, product_id: str):
        parser = reqparse.RequestParser()
        parser.add_argument("text")
        parser.add_argument("name")
        kwargs = parser.parse_args()
        msg = db_actions.add_review_product(product_id, **kwargs)
        responce = jsonify(msg)
        responce.status_code = 200
        return responce


class UserAPI(Resource):
    def post(self, product_id: str):
        parser = reqparse.RequestParser()
        parser.add_argument("name")
        kwargs = parser.parse_args()
        msg = db_actions.buy_product(product_id, **kwargs)
        responce = jsonify(msg)
        responce.status_code = 201
        return responce

api.add_resource(ProductAPI, "/api/products/", "/api/products/<product_id>/")
api.add_resource(UserAPI, "/api/users/<product_id>/")


if __name__ == "__main__":
    app.run(debug=True, port=3000)