
from flask import Flask, request, jsonify

from db import *
# from order import Orders, order_schema, Orders_schema
from users import Users
# , users_schema, user_schema
# from categories import Categories
# from products import Products
# from order_products_association import OrderProductsAssociation

app = Flask(__name__)
#DATABASE RELATIONSHIPS
app.config['SQLALCHEMY_DATABASE_URI'] ="postgresql://Amee@localhost:5432/relationships"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

init_db(app, db)

def create_all():
  with app.app_context():
    print("Creating tables...")
    db.create_all()
    print("All done!")

def populate_object(obj, data_dictionary):
  fields = data_dictionary.keys()
  for field in fields:
    if getattr(obj, field): 
      setattr(obj, field, data_dictionary[field])

@app.route('/user/add', methods=['POST'] )
def user_add():
  post_data = request.json
  if not post_data:
    post_data = request.form


  first_name = post_data.get('first_name')
  last_name = post_data.get('last_name')
  email = post_data.get('email')
  street_address = post_data.get('street_address')
  phone = post_data.get('phone')
  city = post_data.get('city')
  state = post_data.get('state')
  postal_code = post_data.get('postal_code')

  # active = post_data.get('active')
  # orders = post_data.get('orders')

  add_user( first_name, last_name, email, street_address, phone, city, state, postal_code)
   

  return jsonify("User created"), 201

def add_user( first_name, last_name, email, street_address, phone, city, state, postal_code): 
  new_user = Users( first_name, last_name, email, street_address, phone, city, state, postal_code)
  
  db.session.add(new_user)
  db.session.commit()

# @app.route('/order/add', methods=['POST'] )
# def order_add():
#   post_data = request.json
#   if not post_data:
#     post_data = request.form
#   order_id = post_data.get('order_id')
#   user_id = post_data.get('user_id')
#   order_date = post_data.get('order_date')
#   ship_date = post_data.get('ship_date')
#   order_total_price = post_data.get('order_total_price')
#   order_completed = post_data.get('order_completed')
#   add_order(order_id, user_id, order_date, ship_date, order_total_price, order_completed)

#   return jsonify("Created Order"), 201

# def add_order(order_id, user_id, order_date, ship_date, order_total_price, order_completed):
#   new_order = Orders(order_id, user_id, order_date, ship_date, order_total_price, order_completed)
#   db.session.add(new_order)
#   db.session.commit()

# @app.route('/users/get', methods=['GET'] )
# def get_all_active_users():
#   results = db.session.query(Users).filter(Users.active == True).all()

#   if results:
#     return jsonify(users_schema.dump(results)),200

#   else:
#     return jsonify("No users found"),400

# @app.route('/org/get', methods=['GET'])
# def get_all_active_orgs():
#   results = db.session.query(Organizations).filter(Organizations.active == True).all()

#   if results:
#     return jsonify(organizations_schema.dump(results)),200

#   else:
#     return jsonify("No organizations found"),400

# @app.route('/user_by_id/<user_id>', methods=['GET'])
# def get_user_by_id(user_id):
#   results = db.session.query(Users).filter(Users.user_id == user_id).first()

#   if results:
#     return jsonify(user_schema.dump(results)),200

#   else:
#     return jsonify("No user found"),400

# @app.route('/org_by_id/<org_id>', methods=['GET'])
# def get_org_by_id(org_id):
#   results = db.session.query(Organizations).filter(Organizations.org_id == org_id).first()

#   if results:
#     return jsonify(organization_schema.dump(results)),200

#   else:
#     return jsonify("No organization found"),400

# @app.route('/user/update/<user_id>', methods=['POST', 'PUT'])
# def update_user(user_id):
#   results = db.session.query(Users).filter(Users.user_id == user_id).first()

#   new_data = request.form if request.form else request.json
#   if new_data:
#     new_data = dict(new_data)
#   else:
#     return jsonify('No values to change')

#   if not results:
#     return ('User not found'), 404

#   populate_object(results, new_data)
#   db.session.commit()

#   return jsonify ("User updated"), 201

# @app.route('/org/update/<org_id>', methods=['POST', 'PUT'])
# def update_org(org_id):
#   results = db.session.query(Organizations).filter(Organizations.org_id == org_id).first()

#   new_data = request.form if request.form else request.json
#   if new_data:
#     new_data = dict(new_data)
#   else:
#     return jsonify('No values to change')

#   if not results:
#     return ('Organization not found'), 404

#   populate_object(results, new_data)
#   db.session.commit()

#   return jsonify ("Organization updated"), 201

# @app.route('/org/activate/<org_id>', methods=['GET'] )
# def org_activate(org_id):
#   results = db.session.query(Organizations).filter(Organizations.org_id == org_id).first()
#   results.active=True
#   db.session.commit()
#   return jsonify('Organization Activated'), 200

# @app.route('/user/activate/<user_id>', methods=['POST'] )
# def user_activate(user_id):
#   results = db.session.query(Users).filter(Users.user_id == user_id).first()
#   results.active=True
#   db.session.commit()
#   return jsonify('User Activated'), 200

# @app.route('/org/deactivate/<org_id>', methods=['GET'] )
# def org_deactivate(org_id):
#   results = db.session.query(Organizations).filter(Organizations.org_id == org_id).first()
#   results.active=False
#   db.session.commit()
#   return jsonify('Organization Deactivated'), 200

# @app.route('/user/deactivate/<user_id>', methods=['POST'] )
# def user_deactivate(user_id):
#   results = db.session.query(Users).filter(Users.user_id == user_id).first()
#   results.active=False
#   db.session.commit()
#   return jsonify('User Deactivated'), 200

# @app.route('/org/delete/<org_id>', methods=['DELETE'] )
# def org_delete(org_id):
#   results = db.session.query(Organizations).filter(Organizations.org_id == org_id).first()
#   db.session.delete(results)
#   db.session.commit()
#   return jsonify('Organization Deleted'), 200

# @app.route('/user/delete/<user_id>', methods=['DELETE'] )
# def user_delete(user_id):
#   results = db.session.query(Users).filter(Users.user_id == user_id).first()
#   db.session.delete(results)
#   db.session.commit()
#   return jsonify('User Deleted'), 200


if __name__ == '__main__':
    create_all()
    app.run(host='0.0.0.0', port="8089")
