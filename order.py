import uuid 
from sqlalchemy.dialects.postgresql import UUID
from db import db
import marshmallow as ma
from datetime import datetime

# from users import UsersSchema


class Orders(db.Model):
    __tablename__='orders'# Foreign key so that it's not looking for an order
    order_id = db.Column(UUID(as_uuid=True),primary_key=True, default= uuid.uuid4)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey('users.user_id'), nullable=False)
    order_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    ship_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    order_total_price = db.Column(db.Integer(), nullable=False)
    order_completed = db.Column(db.Boolean(), default=True)
    # users = db.relationship('Users', back_populates = 'orders')
    products = db.relationship('association', back_populates ='order_id')

    def __init__(self, order_id, user_id, order_date, ship_date, order_total_price, order_completed):
        self.order_id = order_id
        self.user_id = user_id
        self.order_date = order_date
        self.ship_date = ship_date
        self.order_total_price = order_total_price
        self.order_completed = order_completed


class OrdersSchema(ma.Schema):
    class Meta:
        fields = ['order_id', 'user_id', 'order_date', 'ship_date', 'order_total_price', 'order_completed']

    # order = ma.fields.Nested(UsersSchema())
order_schema = OrdersSchema() # always return a dictionary
Orders_schema = OrdersSchema( many=True ) # always going to return a list[]
#exclude=['user_id']