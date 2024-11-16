from flask import Flask
import json
from data.constantes import *
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "hola"


@app.route("/cities")
def getCities():
    with open(CITIES_JSON_FILE, 'r') as file:
        cities = json.load(file)
        return jsonify(cities)
