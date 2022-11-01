import uuid 
from sqlalchemy.dialects.postgresql import UUID
from db import db
import marshmallow as ma


class Products(db.Model):
    __tablename__='products'
    product_id = db.Column(UUID(as_uuid=True),primary_key=True, default= uuid.uuid4)
    product_name = db.Column(db.String(), nullable= False)
    product_description = db.Column(db.String())
    product_total_price = db.Column(db.String(), nullable= False)
    category_id = db.Column(UUID(as_uuid=True),db.ForeignKey('categories.category_id'), nullable=False)
    active = db.Column(db.Boolean(), default=True)
    orders = db.relationship('OrderProductsAssociation',back_populates = 'product_id')
    def __init__(self, product_id, product_name, product_description, product_total_price, category_id, active):
        self.product_id = product_id
        self.product_name = product_name
        self.product_description = product_description
        self.product_total_price = product_total_price
        self.category_id = category_id
        self.active = active


# class ProductsSchema(ma.Schema):
#     class Meta:
#         fields = ['product_id', 'product_name', 'product_description', 'product_total_price','category_id', 'active']


# product_schema = ProductSchema()
# products_schema = ProductSchema( many=True )

# I don't understand the back_populates or the relationships