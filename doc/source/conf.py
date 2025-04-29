# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sys
from pathlib import Path
import toml  # Utilisez `tomllib` si vous êtes en Python 3.11+

# -- Chemins et configuration ------------------------------------------------

# Chemin vers le répertoire racine du projet (remonte de trois niveaux)
project_root = Path(__file__).resolve().parent.parent.parent

# Ajoute le chemin du projet pour importer les modules
sys.path.insert(0, str(project_root / "src"))

# -- Lecture des informations depuis pyproject.toml -------------------------

# Chemin vers le fichier pyproject.toml
pyproject_path = project_root / "pyproject.toml"

# Charge le fichier pyproject.toml
with open(pyproject_path, "r", encoding="utf-8") as f:
    pyproject_data = toml.load(f)

# Extrait les informations du projet
project_info = pyproject_data["project"]

# -- Project information -----------------------------------------------------

project = project_info["name"]
author = project_info["authors"][0]["name"]
copyright = f"2025, {author}"
release = project_info["version"]

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",  # Génère la documentation à partir des docstrings
    "sphinx.ext.viewcode",  # Ajoute des liens vers le code source
    "sphinx_rtd_theme",  # Active le thème ReadTheDocs
    "sphinx_autodoc_typehints",  # Support des annotations de type
    'sphinx.ext.napoleon',      # Pour prendre en charge les docstrings au format Google ou NumPy
]

templates_path = ["_templates"]
exclude_patterns = []

language = "fr"

# -- Options for HTML output -------------------------------------------------

html_theme = "sphinx_rtd_theme"  # Utilise le thème ReadTheDocs
html_static_path = ["_static"]

# -- Options pour les extensions ---------------------------------------------

# Configuration de l'extension autodoc
autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'show-inheritance': True,
}

# Configuration de l'extension napoleon
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = False