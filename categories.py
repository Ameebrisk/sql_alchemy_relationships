import uuid 
from sqlalchemy.dialects.postgresql import UUID
from db import db
import marshmallow as ma

from products import ProductsSchema

# from organizations import OrganizationsSchema


class Categories(db.Model):
    __tablename__='categories'
    category_id = db.Column(UUID(as_uuid=True),primary_key=True, default= uuid.uuid4)
    category_name = name = db.Column(db.String(), nullable= False)
    category_description = category_description = db.Column(db.String())
    active = active = db.Column(db.Boolean(), default=True)

    def __init__(self, category_id, category_name, category_description, active):
        self.category_id = category_id
        self.name = category_name
        self.category_description = category_description
        self.active = active


class CategoriesSchema(ma.Schema):
    class Meta:
        fields = ['category_id', 'category_name', 'category_description', 'active']

    # order = ma.fields.Nested(UsersSchema())
order_schema = CategoriesSchema(ProductsSchema) # always return a dictionary
Orders_schema = CategoriesSchema( many=True ) # always going to return a list[]