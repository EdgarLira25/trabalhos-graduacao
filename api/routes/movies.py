from flask import jsonify, Blueprint, request
from services.controller.movies import MoviesController
from services.models.movies import Movies

movies_blueprint = Blueprint("users", "__name__")


@movies_blueprint.route("/movies/<string:id>", methods=["GET"])
def get_movie(id: str):
    response = MoviesController().select_one_movie(id=id)
    return jsonify(response), 200


@movies_blueprint.route("/movies", methods=["GET"])
def get_all_movies():
    response = MoviesController().select_all_movies()
    return jsonify(response), 200


@movies_blueprint.route("/movie/delete/<string:id>", methods=["DELETE"])
def delete_movie(id: str):
    MoviesController().delete_movie(id)
    return jsonify(msg="Filme deletado com sucesso"), 200


@movies_blueprint.route("/movie/create", methods=["POST"])
def create_movie():
    payload = request.get_json()
    try:
        movie = Movies(**payload)
    except KeyError as error:
        return jsonify(error=f"Erro no envio do objeto {error}"), 400

    MoviesController().insert_movie(movie=movie)

    return jsonify(msg="Usuário criado com sucesso"), 201
