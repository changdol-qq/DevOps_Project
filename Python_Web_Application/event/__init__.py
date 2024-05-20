from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# Flask app 설정
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '250786e4fb334f739c87706c'

# 의존성 확장
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

# Login manager 설정
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"

# 라우트 모듈 임포트 
from event import routes

