"Rotas para SELECTS em SQL"
from flask import jsonify, Blueprint, request
from services.controller.query import QueryController

query = Blueprint("query", "__name__")


@query.errorhandler(Exception)
def error_handler(e: Exception):
    "Handle Genérico Para Erros"
    return jsonify(str(e)), 400


@query.route("/query", methods=["GET"])
def post_query():
    "Rota para teste de query"
    sql_query = request.args.get("query", "")

    if not sql_query:
        return jsonify(str("Resultado Vazio")), 200

    return jsonify(QueryController().execute_generic_query(sql_query)), 200
