from flask import Flask
from flask_cors import CORS
from api.routes import bp
from config.enum import ErrorMessages

app = Flask(__name__)
CORS(app)

app.register_blueprint(bp) 

if __name__ == '__main__':
    """
    This is the main entry point of the application.
    It creates a Flask app, enables CORS, registers the blueprint for API routes,
    and starts the server.
    """
    try:
        app.run()
    except Exception as e:
        print(ErrorMessages.SERVER_IS_NOT_RUNNING.value)
