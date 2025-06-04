import os
import json
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from flask_wtf.file import FileField, FileAllowed
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'devsecretkey'  # changer en production

UPLOAD_FOLDER = os.path.join('static', 'img')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024  # 2MB max

os.chdir("/home/m.lemenn/Bureau/NSI/tp_web/sl29.systeme_solaire_new/src/sl29/systeme_solaire")
# Chargement JSON
with open('data/planets.json', encoding='utf-8') as f:
    PLANETES = json.load(f)

with open('data/satellites.json', encoding='utf-8') as f:
    SATELLITES = json.load(f)

def get_planet_names():
    return [p['name'] for p in PLANETES]

def get_planet_by_name(name):
    for p in PLANETES:
        if p['name'].lower() == name.lower():
            return p
    return None

def get_satellites_for_planet(name):
    return [s['name'] for s in SATELLITES if s['planet'].lower() == name.lower()]

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

# Forms
class PlanetForm(FlaskForm):
    nom_planete = SelectField('Choisissez une planète:', choices=[])
    submit = SubmitField('Afficher')

class UploadForm(FlaskForm):
    image = FileField('Ajouter une image', validators=[FileAllowed(ALLOWED_EXTENSIONS, 'Images uniquement !')])
    submit = SubmitField('Téléverser')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = PlanetForm()
    form.nom_planete.choices = [(p, p) for p in get_planet_names()]

    if form.validate_on_submit():
        return redirect(url_for('planete', nom=form.nom_planete.data))

    return render_template('index.html', form=form)

@app.route('/planete/<nom>', methods=['GET', 'POST'])
def planete(nom):
    planet = get_planet_by_name(nom)
    if not planet:
        flash("Planète inconnue", 'danger')
        return redirect(url_for('index'))

    satellites = get_satellites_for_planet(nom)
    form = UploadForm()

    # Recherche image existante
    image_filename = None
    for ext in ALLOWED_EXTENSIONS:
        path = os.path.join(app.config['UPLOAD_FOLDER'], f"{nom.lower()}.{ext}")
        if os.path.exists(path):
            image_filename = f"{nom.lower()}.{ext}"
            break

    if form.validate_on_submit():
        file = request.files.get('image')
        if file and allowed_file(file.filename):
            filename = secure_filename(f"{nom.lower()}.{file.filename.rsplit('.',1)[1].lower()}")
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            flash("Image téléversée avec succès !", 'success')
            return redirect(url_for('planete', nom=nom))
        else:
            flash("Format d’image non autorisé.", 'danger')

    return render_template('planet.html', planet=planet, satellites=satellites,
                           form=form, image_filename=image_filename)

if __name__ == '__main__':
    # Crée le dossier img s'il n'existe pas
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
