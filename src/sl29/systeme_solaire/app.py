"""Un module pour l'application"""

from flask import Flask, render_template

from sl29.systeme_solaire import planets

app = Flask(__name__)

@app.route("/")
def accueil()->str:
    """Affiche la page d'accueil

    Returns:
        str: le code html de la page d'accueil.
    """
    planetes = planets.get_planets()
    return render_template("index.html", planets = planetes)

# en mode debug, le serveur raffraichit automatiquement les modifications apportées au code
app.run(debug=True)
