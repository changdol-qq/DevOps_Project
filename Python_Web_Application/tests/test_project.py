from event.models import User




def test_app(client, app):
    # 홈 페이지 테스트
    response = client.get("/")
    assert response.status_code == 200

    # 회원가입 기능 테스트
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

    # 로그인 기능 테스트
    client.post("/login", data={'username': 'test', 'password': 'VMware1!'})
    response = client.get("/event")
    assert response.status_code == 200

    # crete 페이지 테스트
    response = client.get("/create")
    assert response.status_code == 200



 