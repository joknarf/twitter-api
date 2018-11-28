# app/__init.py__
from flask import Flask
from flask_restplus import Api

def create_app():
    app = Flask(__name__)

    # Remove the previous code using `@app` and replace it with:
    from .main.controllers import main
    app.register_blueprint(main)

    from .apis.tweets import api as tweets
    api = Api()
    api.add_namespace(tweets)
    api.init_app(app)

    app.config['ERROR_404_HELP'] = False
    return app
