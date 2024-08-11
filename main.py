from flask import Flask
from routes.users import users_blueprint

if __name__ == "__main__":

    app = Flask(__name__)
    app.register_blueprint(users_blueprint)
    app.run(port=8000, debug=False)
