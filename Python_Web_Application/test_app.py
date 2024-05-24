# # test_app.py
# import pytest
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_bcrypt import Bcrypt
# from flask_login import LoginManager, login_user, logout_user, current_user
# from event import app, db
# from event.models import User, Event
# from event.forms import RegisterForm, CreateEventForm

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

# def test_home_page(test_client):
#     response = test_client.get('/')
#     assert response.status_code == 200

# def test_register_form(test_client):
#     form = RegisterForm(username='testuser', email_address='test@test.com', password1='password', password2='password')
#     assert form.validate() == True

# def test_invalid_register_form(test_client):
#     form = RegisterForm(username='t', email_address='invalid', password1='pwd', password2='pwd')
#     assert form.validate() == False

# def test_create_event_form(test_client):
#     form = CreateEventForm(date='2023-05-20', name='Test Event', location='Test Location', price=100, description='Test Description')
#     assert form.validate() == True

# def test_user_model(test_client):
#     user = User(username='testuser', email_address='test@test.com', password='password')
#     db.session.add(user)
#     db.session.commit()
#     queried_user = User.query.filter_by(username='testuser').first()
#     assert queried_user is not None

# def test_event_model(test_client):
#     user = User(username='testuser2', email_address='test2@test.com', password='password')
#     db.session.add(user)
#     db.session.commit()
#     event = Event(date='2023-05-20', name='Test Event', location='Test Location', price=100, description='Test Description', owner_id=user.id)
#     db.session.add(event)
#     db.session.commit()
#     queried_event = Event.query.filter_by(name='Test Event').first()
#     assert queried_event is not None

# def test_login_logout(test_client):
#     user = User(username='loginuser', email_address='login@test.com', password='password')
#     db.session.add(user)
#     db.session.commit()
#     with test_client:
#         login_user(user)
#         assert current_user.is_authenticated == True
#         logout_user()
#         assert current_user.is_authenticated == False

# def test_create_event_route(test_client):
#     user = User(username='createeventuser', email_address='createevent@test.com', password='password')
#     db.session.add(user)
#     db.session.commit()
#     with test_client:
#         login_user(user)
#         response = test_client.post('/create', data=dict(date='2023-05-20', name='Test Event', location='Test Location', price=100, description='Test Description'), follow_redirects=True)
#         assert response.status_code == 200
#         event = Event.query.filter_by(name='Test Event').first()
#         assert event is not None

# # import pytest
# # from event import app
# # from flask import url_for

# # @pytest.fixture
# # def client():
# #     return app.test_client()

# # def test_home_page(client):
# #     response = client.get(url_for('home_page'))
# #     assert response.status_code == 200

# # def test_register_page(client):
# #     response = client.get(url_for('register_page'))
# #     assert response.status_code == 200

# # def test_login_page(client):
# #     response = client.get(url_for('login_page'))
# #     assert response.status_code == 200

# # def test_create_page(client, logged_in_user):
# #     response = client.get(url_for('create_page'))
# #     assert response.status_code == 200