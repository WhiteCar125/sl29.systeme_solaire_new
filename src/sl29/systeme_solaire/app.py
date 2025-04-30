"""Un module pour l'application"""

import json
from flask import Flask, render_template, request


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
    planet_data = get_planet_by_id(planet_id)
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

    # A FAIRE

    # récupérer l'id du sattelite depuis la requete
    # Si l'id n'est pas trouvé, retourner un message d'erreur et un status 404

    # Récuperer les données du satellite
    # Si aucune donnée trouvée, retourner un message d'erreur et un status 404

    # récupérer les données de la planète associée.

    # retourner le template 'satellite.html' avec les variables:
    # - satellite
    # - planet


def get_planet_by_id(planet_id):
    """Version avec boucle for pour remplacer next()"""
    for planet in planets:
        if planet['id'] == planet_id:
            return planet
    return None  # Si aucune planète trouvée

if __name__ == '__main__':
    app.run(debug=True)
