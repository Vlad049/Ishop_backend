import os

from flask import Flask, jsonify
from flask_restful import Resource, request
from dotenv import load_dotenv

from src.database.base import db
from src.data import parse_products


load_dotenv()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_URI")
db.init_app(app)


with app.app_context():
    # db.create_all()
    parse_products.get_products()