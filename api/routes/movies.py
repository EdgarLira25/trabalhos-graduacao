"Rotas para o CRUD da tabela filmes"
from flask import jsonify, Blueprint, request
from services.controller.movies import MoviesController
from services.models.movies import Movies

movies_blueprint = Blueprint("users", "__name__")


@movies_blueprint.route("/movies/<string:movie_id>", methods=["GET"])
def get_movie(movie_id: str):
    "Rota para seleção de um filme"
    response = MoviesController().select_one_movie(movie_id=movie_id)
    return jsonify(response), 200


@movies_blueprint.route("/movies", methods=["GET"])
def get_all_movies():
    "Rota retorna todos filmes"
    response = MoviesController().select_all_movies()
    return jsonify(response), 200


@movies_blueprint.route("/movie/delete/<string:movie_id>", methods=["DELETE"])
def delete_movie(movie_id: str):
    "Rota para deleção de filmes"
    MoviesController().delete_movie(movie_id)
    return jsonify(msg="Filme deletado com sucesso"), 200


@movies_blueprint.route("/movie/create", methods=["POST"])
def create_movie():
    """Payload esperado segue o model em services/models/movies"""
    payload = request.get_json()
    try:
        movie = Movies(
            movie_id=payload["movie_id"],
            title=payload["title"],
            year=payload["year"],
            type=payload["type"],
            minutes=payload["minutes"],
            rating=payload["rating"],
            votes=payload["votes"],
        )
    except KeyError as error:
        return jsonify(error=f"Erro no envio do objeto {error}"), 400

    MoviesController().insert_movie(movie=movie)

    return jsonify(msg="Usuário criado com sucesso"), 201
