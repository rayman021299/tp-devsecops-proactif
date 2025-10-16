from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Bonjour ! Bienvenue sur notre projet de TP DevSecOps."

# On ajoutera des vulnérabilités ici plus tard !

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')