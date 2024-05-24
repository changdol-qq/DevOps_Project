import pytest
from event import create_app, db
# 현재 파일의 디렉토리 경로를 기준으로 event 디렉토리를 경로에 추가

@pytest.fixture()
def app():
    app = create_app("sqlite://")
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    with app.app_context():
        db.create_all()

    yield app
    with app.app_context():
        db.drop_all()

@pytest.fixture()
def client(app):
    return app.test_client()