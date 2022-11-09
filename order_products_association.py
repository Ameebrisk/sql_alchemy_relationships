import marshmallow as ma 
from db import db
from sqlalchemy.dialects.postgresql import UUID

class OrderProductsAssociation(db.Model):
    __tablename__='association'
    order_id = db.Column('order_id',UUID(as_uuid=True), db.ForeignKey('orders.order_id'), primary_key=True)
    product_id = db.Column('product_id',UUID(as_uuid=True), db.ForeignKey('products.product_id'), primary_key=True)
    quantity = db.Column ('quantity',db.Integer(), nullable=False)
    order = db.relationship('Orders',back_populates = 'orders')
    product = db.relationship('Products', back_populates = 'products')
  
    def __init__(self, order_id, product_id, quanitity):
      self.order_id = order_id
      self.product_id = product_id
      self.quanitity = quanitity

#If I add additional fields into an association table then I want to turn it into a model.

class OrderProductsAssociationSchema(ma.Schema):
  class Meta:
    fields = ['order_id', 'product_id', 'quantity']
#OrderSchema, ProductSchema
association_schema = OrderProductsAssociationSchema()
associations_schema = OrderProductsAssociationSchema(many=True)

  