from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Bonjour ! Bienvenue sur notre projet de TP DevSecOps."

@app.route('/files')
def list_files():
    directory = request.args.get('dir', '.')
    # La commande 'ls' est concaténée avec une entrée utilisateur sans validation.
    command = "ls -l " + directory
    file_list = os.popen(command).read()
    return f"<pre>{file_list}</pre>"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')