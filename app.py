from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Bonjour ! Bienvenue sur notre projet de TP DevSecOps."

@app.route('/files')
def list_files():
    # Allow only subdirectories of the current directory, and sanitize input
    import re
    directory = request.args.get('dir', '.')
    if not re.fullmatch(r'[\w\-/.]+', directory) or '..' in directory:
        return "Invalid directory name.", 400
    base_path = os.path.abspath('.')
    target_path = os.path.abspath(os.path.join(base_path, directory))
    if not target_path.startswith(base_path):
        return "Directory access denied.", 403
    try:
        files = os.listdir(target_path)
        file_list = ""
        for f in files:
            full_path = os.path.join(target_path, f)
            stats = os.stat(full_path)
            file_list += f"{f}\tSize: {stats.st_size} bytes\n"
    except Exception as e:
        return f"Error accessing directory: {e}", 500
    return f"<pre>{file_list}</pre>"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')