from flask import Flask, Blueprint, render_template
import os

def views_site():
    views = Blueprint('views', __name__)

    @views.route('/')
    def home():
        return render_template('base.html')
    
    return views

def auth_site():
    auth = Blueprint('auth', __name__)

    @auth.route("/login")
    def login():
        return "<p>Login</p>"

    @auth.route("/logout")
    def logout():
        return "<p>Logout</p>"

    @auth.route("/sign-up")
    def sign_up():
        return "<p>Sign Up</p>"
    
    return auth


def create_app():
    with open(os.path.join('website','secret_key.0'), "r", encoding="utf-8") as sc:
        secret_key = sc.read()
    
    app = Flask(__name__)
    app.config['SECRET_KEY'] = secret_key
    
    app.register_blueprint(views_site(), url_prefix="/")
    app.register_blueprint(auth_site(), url_prefix="/")
    
    return app
