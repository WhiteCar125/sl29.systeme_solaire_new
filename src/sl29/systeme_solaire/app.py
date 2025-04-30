"""Un module pour l'application"""

from flask import Flask, render_template, request
import json

app = Flask(__name__)

# Chargement des données
with open('data/planets.json', 'r', encoding='utf-8') as f:
    planets = json.load(f)

with open('data/satellites.json', 'r', encoding='utf-8') as f:
    satellites = json.load(f)

@app.route('/')
def index():
    """Page d'accueil montrant comment les paramètres fonctionnent"""
    return render_template('index.html', planets=planets)

@app.route('/planete')
def show_planet():
    """Démontre l'utilisation de request.args.get()"""
    # Récupération du paramètre 'id' de la requête
    planet_id = request.args.get('id', type=int)

    # Vérification si le paramètre existe et est valide
    if planet_id is None:
        return "Erreur: Le paramètre 'id' est requis. Exemple: /planete?id=3", 400

    # Recherche de la planète
    planet_data = next((p for p in planets if p['id'] == planet_id), None)
    if not planet_data:
        return f"Erreur: Aucune planète trouvée avec l'ID {planet_id}", 404

    # Récupération des satellites
    planet_satellites = [s for s in satellites if s['planetId'] == planet_id]

    return render_template('planet.html',
                         planet=planet_data,
                         satellites=planet_satellites,
                         request_args=dict(request.args))  # Pour démo pédagogique

@app.route('/satellite')
def show_satellite():
    """Montre comment gérer plusieurs paramètres"""
    satellite_id = request.args.get('id', type=int)

    if satellite_id is None:
        return "Erreur: Le paramètre 'id' est requis. Exemple: /satellite?id=1", 400

    satellite_data = next((s for s in satellites if s['id'] == satellite_id), None)
    if not satellite_data:
        return f"Erreur: Aucun satellite trouvé avec l'ID {satellite_id}", 404

    planet_data = next((p for p in planets if p['id'] == satellite_data['planetId']), None)

    return render_template('satellite.html',
                         satellite=satellite_data,
                         planet=planet_data,
                         request_args=dict(request.args))  # Pour démo pédagogique

if __name__ == '__main__':
    app.run(debug=True)
