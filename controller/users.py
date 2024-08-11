from database.manager import DatabaseManager


class UserController:

    def __init__(self) -> None:
        pass

    def select_all_users(self):
        return DatabaseManager().execute_select_all(query="SELECT * FROM usuario;")

    def create_user(self, nome: str, senha: str):
        return DatabaseManager().execute_statement(
            f"""INSERT INTO usuario (nome, senha) VALUES ('{nome}', '{senha}');"""
        )

    def delete_user(self, id: int):
        DatabaseManager().execute_statement(f"DELETE FROM usuario WHERE id = {id};")
