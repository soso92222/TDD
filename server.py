import json
from flask import Flask, render_template, request, redirect, flash, url_for, abort

# --- Chargement des données ---
def loadClubs():
    """Charge les clubs depuis le fichier JSON."""
    with open('clubs.json') as c:
        listOfClubs = json.load(c)['clubs']
        return listOfClubs

def loadCompetitions():
    """Charge les compétitions depuis le fichier JSON."""
    with open('competitions.json') as comps:
        listOfCompetitions = json.load(comps)['competitions']
        return listOfCompetitions


# --- Configuration de l'application Flask ---
app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()


# --- ROUTE 1 : Page d'accueil ---
@app.route('/')
def index():
    """Affiche la page d'accueil avec le formulaire de connexion."""
    return render_template('index.html')


# --- ROUTE 2 : Résumé du club après connexion ---
@app.route('/showSummary', methods=['POST'])
def showSummary():
    """Affiche la page de bienvenue après identification par email."""
    try:
        club = [club for club in clubs if club['email'] == request.form['email']][0]
    except IndexError:
        flash("Email inconnu. Veuillez réessayer.")
        return redirect(url_for('index'))
    
    return render_template('welcome.html', club=club, competitions=competitions)


# --- ROUTE 3 : Réservation d'une place ---
@app.route('/book/<competition>/<club>')
def book(competition, club):
    """Permet de réserver une place pour une compétition."""
    foundClub = next((c for c in clubs if c['name'] == club), None)
    foundCompetition = next((c for c in competitions if c['name'] == competition), None)

    if foundClub and foundCompetition:
        return render_template('booking.html', club=foundClub, competition=foundCompetition)
    else:
        flash("Something went wrong - please try again.")
        return render_template('welcome.html', club=club, competitions=competitions)


# --- ROUTE 4 : Achat de places ---
@app.route('/purchasePlaces', methods=['POST'])
def purchasePlaces():
    """Gère l'achat des places et met à jour le nombre de places restantes."""
    competition = next((c for c in competitions if c['name'] == request.form['competition']), None)
    club = next((c for c in clubs if c['name'] == request.form['club']), None)
    placesRequired = int(request.form['places'])

    if competition and club:
        competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - placesRequired
        flash('Great - booking complete!')
    else:
        flash('Erreur - données invalides.')

    return render_template('welcome.html', club=club, competitions=competitions)


# --- ROUTE 5 : Page ADMIN (pour les tests) ---
@app.route('/admin', methods=['POST'])
def admin():
    """Vérifie les identifiants envoyés depuis un formulaire POST."""
    email = request.form.get('email')
    password = request.form.get('password')
    print(password)
    print(email)
    print(request.form)
    # Vérification des identifiants
    if email == 'admin@gmail.com' and password == 'admin92230':
        return "Bienvenue admin", 200  # OK
    else:
        abort(403)  # Accès refusé


@app.route('/admin', methods=['GET'])
def admin_page():
    """Empêche l'accès direct à la page admin sans authentification."""
    abort(403)


# --- ROUTE 6 : Déconnexion ---
@app.route('/logout')
def logout():
    """Retour à la page d'accueil."""
    return redirect(url_for('index'))


# --- Point d'entrée principal ---
if __name__ == '__main__':
    app.run(debug=True)
