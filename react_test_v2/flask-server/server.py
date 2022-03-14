from json.tool import main
from unicodedata import name
from crypt import methods
from flask import Flask, jsonify, request
from models.db import app, db
from schemas.ma import ma
from models.category import Category
from schemas.categorySchema import CategorySchema
import json

db.create_all()

# One response
category_schema = CategorySchema()

# Many responses
categories_schema = CategorySchema(many=True)

# Members API route

@app.route("/members")
def members():
    return {"members":["Member1", "Member2", "Member3"]}

@app.route("/miembros")
def miembros():
    return {"members":"camilo","email":"camilo@mail.com"}

# GET x ID
@app.route('/category/<id>', methods=['GET'])
def get_category_by_id(id):
    one_category = Category.query.get(id)
    return category_schema.jsonify(one_category)

# GET
@app.route('/category', methods=['GET'])
def get_categories():
    all_categories = Category.query.all()
    result = categories_schema.dump(all_categories)
    return jsonify(results=result)

# POST
@app.route('/category', methods=['POST'])
def insert_category():
    data = request.get_json(force=True)
    cat_nom = data['cat_nom']
    cat_desp = data['cat_desp']

    new_register = Category(cat_nom, cat_desp)

    db.session.add(new_register)
    db.session.commit()
    return category_schema.jsonify(new_register)

if __name__ == "__main__":
    app.run(debug=True)