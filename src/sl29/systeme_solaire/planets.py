"""Un module pour les planètes"""

import json
from typing import Dict, Tuple

def _get_planets_from_datas()->Tuple[Dict, ...]:
    """
    Retourne la liste des planètes sous forme de dictionnaire.
    Returns:
        Tuple[Dict, ...]: Les planètes
    """
    import os 
    print(f"=====>{os.getcwd()}")
    with open('src/sl29/systeme_solaire/datas/planets.json', encoding='utf-8') as json_file:
        planets = json.load(json_file)
        return planets

PLANETS = _get_planets_from_datas()

def get_planets()->Tuple[Dict,...]:
    """
    Retourne les planètes classées par leur distance au soleil

    Returns:
        Tuple[Dict, ...]: Les planètes
    """
    planets = list(PLANETS)
    sorted_planets = sorted(planets, key=lambda p:p['distanceFromSun'])
    return tuple(sorted_planets)
