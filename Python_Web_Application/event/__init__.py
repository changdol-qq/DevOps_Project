from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# Flask 확장 초기화
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()

def create_app(database_uri='sqlite:///market.db'):
    # Flask 앱 설정 및 생성
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
    app.config['SECRET_KEY'] = '250786e4fb334f739c87706c'

    # 확장 초기화
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    # 로그인 매니저 설정
    login_manager.login_view = "login_page"
    login_manager.login_message_category = "info"

    # 라우트 등록
    with app.app_context():
        from . import routes # 앱 컨텍스트 내에서 라우트 임포트

    return app




