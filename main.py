from flask import Flask
from api.routes.movies import movies_blueprint

if __name__ == "__main__":

    app = Flask(__name__)
    app.register_blueprint(movies_blueprint)
    app.run(port=8000, debug=False)
