from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World! Esta es un cambio'

@app.route('/about')
def about():
    return 'About'