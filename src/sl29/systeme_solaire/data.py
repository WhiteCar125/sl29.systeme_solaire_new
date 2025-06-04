import json
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

def load_planets():
    with open(os.path.join(DATA_DIR, 'planetes.json'), encoding='utf-8') as f:
        return json.load(f)

def load_satellites():
    with open(os.path.join(DATA_DIR, 'satellites.json'), encoding='utf-8') as f:
        return json.load(f)

def get_planet_names():
    return [planet["name"] for planet in load_planets()]

def get_planet_info(name):
    for planet in load_planets():
        if planet["name"].lower() == name.lower():
            return planet
    return None

def get_satellites_for_planet(name):
    name = name.lower()
    return [sat["name"] for sat in load_satellites() if sat["planet"].lower() == name]
