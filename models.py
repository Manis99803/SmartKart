import datetime
from app import db
from sqlalchemy import Integer, ForeignKey, String, Column, Float,between
from flask_login import UserMixin
from app import login
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	phno = db.Column(db.Integer, default = 123123)
	name = db.Column(db.String(100), nullable=True, default = "mayank")
	member_since = db.Column(db.DateTime(), default=datetime.datetime.now)
	address = db.Column(db.String(200), nullable = True, default = "address")
	order = db.relationship('Order', backref='User')
	username = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	password_hash = db.Column(db.String(128))
	cart_in = db.relationship('Cart', backref = 'User')
	rating = db.relationship('Rating', backref = 'User')
	shipment = db.relationship('Shipment', backref = 'User')
	order_list = db.relationship('OrderList', backref = 'User')

	def __repr__(self):
	    return '<User {}>'.format(self.username)

	def set_password(self, password):
	    self.password_hash = generate_password_hash(password)

	def check_password(self, password):
	    return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class Order(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	date = db.Column(db.Date, default = datetime.datetime.now )
	cust_id = db.Column(db.Integer, ForeignKey(User.id, ondelete='CASCADE'))
	price = db.Column(db.Float, nullable = True)
	order_list = db.relationship('OrderList', backref = 'Order')
	status =  db.Column(db.String(128))
	shipment = db.relationship('Shipment', backref = 'Order')

	def __str__(self):
		return str(self.id)


class Product(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	price = db.Column(db.Float, nullable = False)
	type = db.Column(db.String(20), nullable = False)
	brand = db.Column(db.String(40), nullable = True)
	Color = db.Column(db.String(40), nullable = True)
	size = db.Column(db.Float, nullable = True)
	order_list = db.relationship('OrderList', backref='Product')
	cart_in = db.relationship('Cart', backref = 'Product')
	stock = db.relationship('Stock', backref = 'Product')
	rating = db.relationship('Rating', backref = 'Product')
	clothes = db.relationship('Clothes', backref = 'Product', foreign_keys = '[Clothes.size, Clothes.size]')
	Electronics = db.relationship('Electronics', backref = 'Product')
	books = db.relationship('Books', backref = 'Product')

	def __str__(self):
		return str(self.id)

class OrderList(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	order_id = db.Column(db.Integer, ForeignKey(Order.id, ondelete='CASCADE'))
	p_id = db.Column(db.Integer, ForeignKey(Product.id, ondelete='CASCADE'))
	quantity = db.Column(db.Integer, nullable = False, default = 1)
	c_id = db.Column(db.Integer, ForeignKey(User.id, ondelete='CASCADE'),nullable = False)
	used = db.Column(db.Boolean, default = False)

class Supplier(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(111), nullable = True)
	phno = db.Column(db.Integer, nullable = False)
	address = db.Column(db.String(100), nullable = True)
	stock = db.relationship('Stock', backref = 'Supplier')
	shipment = db.relationship('Shipment', backref = 'Supplier')
	def __str__(self):
		return self.name

class Shipper(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(111), nullable = True)
	phno = db.Column(db.Integer, nullable = False)
	address = db.Column(db.String(100), nullable = True)
	shipment = db.relationship('Shipment', backref = 'Shipper')

	def __str__(self):
		return self.name

class Shipment(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	sup_id = db.Column(db.Integer, ForeignKey(Supplier.id,ondelete='CASCADE'), nullable = True)
	# sup_add = db.Column(db.String(100), ForeignKey(Supplier.address,ondelete='CASCADE'), nullable = False)
	cust_id = db.Column(db.Integer, ForeignKey(User.id,ondelete='CASCADE') )
	# cust_add = db.Column(db.String(100), ForeignKey(User.address,ondelete='CASCADE'))
	order_id = db.Column(db.Integer, ForeignKey(Order.id,ondelete='CASCADE'))
	ship_id = db.Column(db.Integer, ForeignKey(Shipper.id,ondelete='CASCADE'))

class Stock(db.Model):
	sup_id = db.Column(db.Integer, ForeignKey(Supplier.id,ondelete='CASCADE'), primary_key = True)
	prod_id = db.Column(db.Integer, ForeignKey(Product.id,ondelete='CASCADE'), primary_key = True)
	quantity = db.Column(db.Integer, nullable = False)

class Rating(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	prod_id = db.Column(db.Integer, ForeignKey(Product.id,ondelete='CASCADE'), nullable = False)
	stars= db.Column(db.Integer, nullable = False)
	rated_by = db.Column(db.String(100), ForeignKey(User.id,ondelete='CASCADE'))
	comments = db.Column(db.String(100), nullable = False)

class Cart(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	prod_id = db.Column(db.Integer, ForeignKey(Product.id,ondelete='CASCADE'), nullable = False)
	customer_id= db.Column(db.Integer, ForeignKey(User.id,ondelete='CASCADE'), nullable = False)

class Electronics(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(111), nullable = True)
	prod_type = db.Column(db.String(100), nullable = False)
	prod_id = db.Column(db.String(100), ForeignKey(Product.id,ondelete='CASCADE'), nullable = False)
	processor= db.Column(db.String(10) , nullable = False)
	ram = db.Column(db.String(10) , nullable = False)
	external_harddrive = db.Column(db.String(10) , nullable = False)
	os_name = db.Column(db.String(10) , nullable = False)

class Clothes(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(111), nullable = True)
	prod_type = db.Column(db.String(100), nullable = False)
	prod_type = db.Column(db.String(100), nullable = False)
	prod_id = db.Column(db.String(100), ForeignKey(Product.id,ondelete='CASCADE'), nullable = False)
	color = db.Column(db.String(10), ForeignKey(Product.Color,ondelete='CASCADE'), nullable = False)
	size = db.Column(db.String(10), ForeignKey(Product.size,ondelete='CASCADE'), nullable = False)

class Books(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(111), nullable = True)
	prod_type = db.Column(db.String(100), nullable = False)
	prod_type = db.Column(db.String(100), nullable = False)
	prod_id = db.Column(db.String(100) ,ForeignKey(Product.id,ondelete='CASCADE'))
	publisher = db.Column(db.String(10) , nullable = False)
	author = db.Column(db.String(10) , nullable = False)
	Langauage = db.Column(db.String(10) , nullable = False)



# @login.user_loader
# def load_user(id):
#     return User.query.get(int(id))
