import pytest
from server import app, loadClubs, loadCompetitions

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200

        
def _server_start_index(client):
    rv = client.get('/')
    assert rv.status_code == 200
    template = app.jinja_env.get_template('index.html')
    assert template.render() == rv.get_data(as_text=True) 

def _pages_return_correct_html_get(client, route, page):
    rv = client.get(route, follow_redirects = True)
    assert rv.status_code == 200
    template = app.jinja_env.get_template(page)
    assert template.render() == rv.get_data(as_text=True) 
    
    
def _login_club(client, email='admin@irontemple.com'):
    rv = client.post('/showSummary', data = dict(email = email), follow_redirects = True)
    assert rv.status_code == 200
    assert rv.data.decode().find("Welcome, {}".format(email)) != -1


def test_cannot_access_welcome_without_form():
    """Impossible d'accéder à la page welcome sans saisie"""
    tester = app.test_client()
    response = tester.post('/showSummary', data={'email': ''}, follow_redirects=True)

    # Redirigé vers la page d'accueil ou erreur
    assert response.status_code in [302, 200]
    assert b"Email inconnu" in response.data or b"<form" in response.data


def test_cannot_access_admin_page_directly():
    """Impossible d'accéder à /admin sans POST (GET = refusé)"""
    tester = app.test_client()
    response = tester.get('/admin')
    assert response.status_code == 403