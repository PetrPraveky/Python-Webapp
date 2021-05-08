from flask import Flask
import os

def create_app():
    with open(os.path.join('website','secret_key.0'), "r", encoding="utf-8") as sc:
        secret_key = sc.read()
    
    app = Flask(__name__)
    app.config['SECRET_KEY'] = secret_key
    
    return app
