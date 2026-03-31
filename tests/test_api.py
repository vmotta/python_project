from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health():
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json()['status'] == 'ok'


def test_register_and_login():
    payload = {
        'email': 'tester@example.com',
        'full_name': 'Tester',
        'password': 'secret123'
    }
    register = client.post('/auth/register', json=payload)
    assert register.status_code in (200, 400)

    login = client.post(
        '/auth/login',
        data={'username': payload['email'], 'password': payload['password']},
        headers={'Content-Type': 'application/x-www-form-urlencoded'}
    )
    assert login.status_code == 200
    assert 'access_token' in login.json()
