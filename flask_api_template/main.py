"Inicializa FLASK API"
from flask import Flask
from flask_cors import CORS
from api.routes.query import query
from api.routes.movies import movies_blueprint

if __name__ == "__main__":

    app = Flask(__name__)
    CORS(app, origins="*")
    app.register_blueprint(movies_blueprint)
    app.register_blueprint(query)
    app.run(port=8000, debug=False)
