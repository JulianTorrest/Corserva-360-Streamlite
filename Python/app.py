from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@db:5432/database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Model definition
class SaleOrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    productName = db.Column(db.String(255), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<SaleOrderItem {self.productName}>'

@app.route('/saleOrderItems', methods=['GET'])
def get_sale_order_items():
    sale_order_items = SaleOrderItem.query.all()
    return jsonify([item.__dict__ for item in sale_order_items]), 200

@app.route('/saleOrderItems', methods=['POST'])
def create_sale_order_item():
    data = request.json
    new_sale_order_item = SaleOrderItem(productName=data['productName'], quantity=data['quantity'], price=data['price'])
    db.session.add(new_sale_order_item)
    db.session.commit()
    return jsonify({'message': 'Sale Order Item created successfully'}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
