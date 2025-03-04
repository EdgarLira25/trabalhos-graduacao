"Camada de controller para o CRUD referente a tabela filmes"
from services.database.manager import DatabaseManager
from services.models.movies import Movies


class MoviesController:
    "Camada de Controller da rota movie"

    def __init__(self) -> None:
        pass

    def select_one_movie(self, movie_id: str) -> Movies | None:
        "Seleciona um filme a partir de um ID"
        result = DatabaseManager().execute_select_one(
            f"SELECT * FROM movies WHERE movie_id = '{movie_id}'"
        )

        if not result:
            return None

        return Movies(**result)

    def select_all_movies(self) -> list[Movies]:
        "Retorna todos os Filmes do Database"
        return [
            Movies(**movie)
            for movie in DatabaseManager().execute_select_all(
                query="SELECT * FROM movies;"
            )
        ]

    def insert_movie(self, movie: Movies):
        "Insere filmes no database"
        DatabaseManager().execute_statement(
            f"""
                INSERT INTO movies (movie_id, title, year, type, minutes, rating, votes)
                VALUES (
                        '{movie["movie_id"]}', '{movie["title"]}', {movie["year"]},
                        '{movie["type"]}', {movie["minutes"]}, {movie["rating"]},
                         {movie["votes"]}
                        );
            """
        )

    def delete_movie(self, movie_id: str):
        "Deleta filmes do database"
        DatabaseManager().execute_statement(
            f"DELETE FROM usuario WHERE movie_id = {movie_id};"
        )
