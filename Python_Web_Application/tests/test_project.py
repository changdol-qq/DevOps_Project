from event.models import User
from flask import url_for
def test_app(client, app):
    # 홈 페이지 테스트
    response = client.get("/")
    assert response.status_code == 200


    # 회원가입 테스트
    response = client.post('/register', data={
        "email_address": "test@test.com",
        "password1": "VMware1!",
        "password2": "VMware1!",
        "username": "test"
    }, follow_redirects=True)
    assert response.status_code == 200
    with app.app_context():
        assert User.query.count() == 1
        assert User.query.first().email_address == "test@test.com"

    client.post("/login", data={'username': 'test', 'password': 'VMware1!'})
    response = client.get("/event")
    assert response.status_code == 200

    response = client.get("/create")
    assert response.status_code == 200

    response = client.get("/login")
    assert response.status_code == 200



# def test_home(client):
#     response = client.get("/")
#     assert response.status_code ==200

# #회원가입 테스트 
# def test_registration(client, app):
#     response = client.post('/register', data={
#         "email_address": "test@test.com",
#         "password1": "VMware1!",
#         "password2": "VMware1!",
#         "username": "test"
#     }, follow_redirects=True)
#     assert response.status_code == 200
#     with app.app_context():
#         assert User.query.count() == 1
#         assert User.query.first().email_address == "test@test.com"


# from event.forms import RegisterForm, CreateEventForm
# def test_registration(client):
#     response = client.post('/register', data={
#         "email_address": "test@test.com",
#         "password1": "VMware1!",
#         "password2": "VMware1!",
#         "username": "test"
#     }, follow_redirects=True)
    
#     assert response.status_code == 200
#     assert b"Registration successful" in response.data
# @pytest.fixture(scope='module')
# def test_client():
#     flask_app = app
#     flask_app.config['TESTING'] = True
#     flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_market.db'
    
#     with flask_app.test_client() as testing_client:
#         with flask_app.app_context():
#             db.create_all()
#             yield testing_client
#             db.drop_all()



# def test_register_form(client):
#     
#     assert form.validate() == True



    
    # assert b"Registration successful" in response.data
 