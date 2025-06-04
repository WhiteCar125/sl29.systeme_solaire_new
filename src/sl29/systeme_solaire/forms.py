from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from flask_wtf.file import FileField, FileAllowed
from data import get_planet_names

class PlanetForm(FlaskForm):
    nom_planete = SelectField("Choisissez une planète :", choices=[(p, p) for p in get_planet_names()])
    submit = SubmitField("Afficher")

class ImageUploadForm(FlaskForm):
    image = FileField("Ajouter une image", validators=[
        FileAllowed(['jpg', 'jpeg', 'png', 'gif', 'webpp'], 'Images uniquement!')
    ])
    submit = SubmitField("Téléverser")
