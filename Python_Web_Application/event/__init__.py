from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# Flask app 설정
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()

def create_app(database_uri='sqlite:///market.db'):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
    app.config['SECRET_KEY'] = '250786e4fb334f739c87706c'

    # 의존성 확장 초기화
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    # Login manager 설정
    login_manager.login_view = "login_page"
    login_manager.login_message_category = "info"

    # 라우트 등록
    with app.app_context():
        from . import routes

    return app

#라우트 모듈 임포트 
# from event import routes

