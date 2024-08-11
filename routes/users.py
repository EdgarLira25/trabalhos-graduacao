from flask import jsonify, Blueprint, request
from controller.users import UserController

users_blueprint = Blueprint("users", "__name__")


@users_blueprint.route("/user/get", methods=["GET"])
def get_user():
    response = UserController().select_all_users()
    return jsonify(response), 200


@users_blueprint.route("/user/delete/<int:id>", methods=["DELETE"])
def delete_user(id: int):
    UserController().delete_user(id)
    return jsonify(msg="Usuário deletado com sucesso"), 200


@users_blueprint.route("/user/create", methods=["POST"])
def create_user():
    payload = request.get_json()

    try:
        nome: str = payload["nome"]
        senha: str = payload["senha"]
    except KeyError as error:
        return jsonify(error=f"Erro no envio do objeto {error}"), 400

    UserController().create_user(nome=nome, senha=senha)

    return jsonify(msg="Usuário criado com sucesso"), 201
