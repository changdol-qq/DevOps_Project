import pytest
import routes 
from event import app
from flask import url_for

@pytest.fixture
def client():
    return app.test_client()

def test_home_page(client):
    response = client.get(url_for('home_page'))
    assert response.status_code == 200

def test_register_page(client):
    response = client.get(url_for('register_page'))
    assert response.status_code == 200

def test_login_page(client):
    response = client.get(url_for('login_page'))
    assert response.status_code == 200

def test_create_page(client, logged_in_user):
    response = client.get(url_for('create_page'))
    assert response.status_code == 200