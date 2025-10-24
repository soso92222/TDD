# Test/test_login.py
# testes l’app comme un vrai utilisateur via HTTP → donc test d’intégration 
from server import app

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200


def test_admin_access_without_credentials():
    """Test : accès refusé avec mauvais Didentifiants"""
    tester = app.test_client()

    # Cas d'erreur → faux identifiants
    response = tester.post('/admin', data={
        'user_name': 'wrong',
        'password': 'wrong'
    })

    # On attend un accès refusé : 403
    assert response.status_code == 403
    assert b'Acc' not in response.data  # pas de "Bienvenue admin"
