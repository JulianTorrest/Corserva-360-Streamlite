from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class SaleOrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    productName = db.Column(db.String(255), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<SaleOrderItem {self.productName}>'
