
from flask import Flask, request, jsonify, abort
from models import Product
from database import db, init_db
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

init_db(app)

# Route to create a product
@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    new_product = Product(
        name=data['name'],
        description=data.get('description'),
        price=data['price'],
        inventory_count=data['inventory_count'],
        category=data['category']
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify(new_product.as_dict()), 201

# Route to read all products or search products
@app.route('/products', methods=['GET'])
def get_products():
    name = request.args.get('name')
    category = request.args.get('category')
    query = Product.query
    if name:
        query = query.filter(Product.name.ilike(f"%{name}%"))
    if category:
        query = query.filter(Product.category.ilike(f"%{category}%"))
    products = query.all()
    return jsonify([product.as_dict() for product in products])

# Route to get a product by ID
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = Product.query.get_or_404(product_id)
    return jsonify(product.as_dict())

# Route to update a product by ID
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = Product.query.get_or_404(product_id)
    data = request.get_json()
    product.name = data.get('name', product.name)
    product.description = data.get('description', product.description)
    product.price = data.get('price', product.price)
    product.inventory_count = data.get('inventory_count', product.inventory_count)
    product.category = data.get('category', product.category)
    db.session.commit()
    return jsonify(product.as_dict())

# Route to delete a product by ID
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({"message": "Product deleted"}), 200

# Route to update inventory in real time
@app.route('/products/<int:product_id>/inventory', methods=['PATCH'])
def update_inventory(product_id):
    product = Product.query.get_or_404(product_id)
    data = request.get_json()
    new_inventory_count = data.get('inventory_count')
    if new_inventory_count is not None:
        product.inventory_count = new_inventory_count
        db.session.commit()
    return jsonify(product.as_dict())

# Route to update product popularity
@app.route('/products/<int:product_id>/popularity', methods=['PATCH'])
def update_popularity(product_id):
    product = Product.query.get_or_404(product_id)
    data = request.get_json()
    new_popularity_score = data.get('popularity_score')
    if new_popularity_score is not None:
        product.popularity_score = new_popularity_score
        db.session.commit()
    return jsonify(product.as_dict())

if __name__ == '__main__':
    app.run(debug=True)
