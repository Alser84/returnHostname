from main import app

def test_home_route():
    responce = app.test_client().get('/')
    assert responce.status_code == 200