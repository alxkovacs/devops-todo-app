from flask import Flask, jsonify
from .database import init_db, db  # Importáld a db-t itt
from .routes import todo_bp, user_bp
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from flask import Response

requests_total = Counter('requests_total', 'Total API requests')

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    init_db(app)

    app.register_blueprint(todo_bp, url_prefix='/todos')
    app.register_blueprint(user_bp, url_prefix='/users')

    @app.before_request
    def before_request():
        requests_total.inc()

    @app.route("/metrics")
    def metrics():
        return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)
    
    # Gyökér végpont definiálása a create_app függvényen belül
    @app.route('/')
    def home():
        return jsonify({"message": "Welcome to the Todo List API"}), 200

    return app

# Exponáljuk a db objektumot a tesztek számára
from .database import db
