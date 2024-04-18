from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '250786e4fb334f739c87706c'
db = SQLAlchemy(app)

from .models import Item
# with app.app_context():
#     db.create_all()

from market import routes

