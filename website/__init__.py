from flask import Flask, Blueprint, render_template, request
import os

def views_site():
    views = Blueprint('views', __name__)

    @views.route('/')       
    def home():
        return render_template('home.html')
    
    return views

def create_app():
    with open(os.path.join('website','secret_key.0'), "r", encoding="utf-8") as sc:
        secret_key = sc.read()
    
    app = Flask(__name__)
    app.config['SECRET_KEY'] = secret_key
    
    app.register_blueprint(views_site(), url_prefix="/")
    
    return app
