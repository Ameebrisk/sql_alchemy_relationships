import uuid 
from sqlalchemy.dialects.postgresql import UUID
from db import db
import marshmallow as ma

# from order import OrdersSchema

class Users(db.Model):
    __tablename__='users'
    user_id = db.Column(UUID(as_uuid=True),primary_key=True, default= uuid.uuid4)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String())
    phone = db.Column(db.String())
    email = db.Column(db.String(), nullable=False, unique=True)
    street_address = db.Column(db.String())
    city = db.Column(db.String())
    state = db.Column(db.String())
    postal_code = db.Column(db.String())
    active = db.Column(db.Boolean(), default=True)
    # orders = db.relationship('Orders', back_populates = 'users')

    def __init__(self, first_name, last_name, email, street_address, phone, city, state, postal_code):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.street_address = street_address
        self.city = city
        self.state = state
        self.postal_code = postal_code
        # self.active = active

# I don't understand the back_populates or the relationships
# Is the orders field in the top need to be called in the __init__???
class UsersSchema(ma.Schema):
    class Meta:
        fields = ['user_id', 'first_name', 'last_name', 'email', 'street_address','phone', 'city','state', 'postal_code', 'active']

    # orders = ma.fields.Nested(OrdersSchema())
user_schema = UsersSchema()
users_schema = UsersSchema( many=True )