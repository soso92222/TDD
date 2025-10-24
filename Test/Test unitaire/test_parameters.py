# Test/test_parameters.py
import pytest
from server import app

def test_home_page(client):
    """Vérifie que la page d'accueil répond correctement"""
    response = client.get('/')
    assert response.status_code == 200


#  Le décorateur doit être ici, au-dessus de test_login_param
@pytest.mark.parametrize("email,password,expected", [
    ("admin@gmail.com", "admin92230", 200),   # OK
    ("admin@gmail.com", "wrong", 403),   # Mauvais mdp
    ("wrong", "admin92230", 403),   # Mauvais user
    ("wrong", "wrong", 403)    # Mauvais user + mdp
])
def test_login_param(email, password, expected):
    """Test paramétré de la connexion admin"""
    tester = app.test_client()
    response = tester.post('/admin', data={
        'email': email,
        'password': password
    })
    assert response.status_code == expected
