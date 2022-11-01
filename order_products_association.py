import marshmallow as ma 
from db import db

order_products_association = db.Table(
  "OrderProductsAssociation",
  db.Model.metadata,
  db.Column('order_id', db.ForeignKey('orders.order_id'), primary_key=True),
  db.Column('product_id', db.ForeignKey('products.product_id'), primary_key=True),
  db.Column ('quantity',db.Integer(), nullable=False)
)