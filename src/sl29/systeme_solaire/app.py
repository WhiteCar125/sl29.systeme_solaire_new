from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def accueil()->str:
    """Affiche la page d'accueil

    Returns:
        str: le code html de la page d'accueil.
    """
    return render_template("index.html")

# en mode debug, le serveur raffraichit automatiquement les modifications apportées au code
app.run(debug=True)
