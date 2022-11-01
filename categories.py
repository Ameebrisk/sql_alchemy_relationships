import uuid 
from sqlalchemy.dialects.postgresql import UUID
from db import db
import marshmallow as ma

# from organizations import OrganizationsSchema


class Categories(db.Model):
    __tablename__='categories'
    category_id = db.Column(UUID(as_uuid=True),primary_key=True, default= uuid.uuid4)
    name = name = db.Column(db.String(), nullable= False)
    category_description = category_description = db.Column(db.String())
    active = active = db.Column(db.Boolean(), default=True)

    def __init__(self, category_id, name, category_description, active):
        self.category_id = category_id
        self.name = name
        self.category_description = category_description
        self.active = active