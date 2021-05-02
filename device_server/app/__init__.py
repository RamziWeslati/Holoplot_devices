from flask import Flask, jsonify
from flask_restx import Api

def create_app(env=None):
    from app.config import config_by_name
    from app.routes import register_routes


    app = Flask(__name__)

    app.config.from_object(config_by_name[env or "test"])

    api = Api(app, title="Flaskerific API", version="0.1.0") #change these not to be hard coded, from conf

    register_routes(api, app)

    @app.route("/health")
    def health():
        return jsonify("healthy")

    return app