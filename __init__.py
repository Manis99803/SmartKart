from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c3209OIOPP901QOU8c2u'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login = LoginManager(app)

from .models import (
	User, Shipper, Stock, Supplier, Order, OrderList,
	Product, Shipment, Rating, Cart,Electronics,Clothes,Books
)

admin = Admin(app, name = 'Smart Kart', template_mode= 'bootstrap3')
admin.add_views(
    ModelView(User, db.session),
    ModelView(Supplier, db.session),
    ModelView(Order, db.session),
    ModelView(OrderList, db.session),
    ModelView(Product, db.session),
    ModelView(Shipper, db.session),
    ModelView(Shipment, db.session),
    ModelView(Stock, db.session),
    ModelView(Rating, db.session),
    ModelView(Cart, db.session),
    ModelView(Electronics, db.session),
    ModelView(Clothes, db.session),
    ModelView(Books, db.session)
)

from app import views