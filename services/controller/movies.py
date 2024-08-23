from services.database.manager import DatabaseManager
from services.models.movies import Movies


class MoviesController:

    def __init__(self) -> None:
        pass
    
    def select_one_movie(self, id: str) -> Movies | None:
        result = DatabaseManager().execute_select_one(f"SELECT * FROM movies WHERE movie_id = '{id}'")

        if not result:
            return None

        return Movies(**result) 

    def select_all_movies(self) -> list[Movies]:
        return [
            Movies(**movie)
            for movie in DatabaseManager().execute_select_all(
                query="SELECT * FROM movies;"
            )
        ]

    def insert_movie(self, movie: Movies):
        DatabaseManager().execute_statement(
            f"""
                INSERT INTO movies (movie_id, title, year, type, minutes, rating, votes)
                VALUES ('{movie["movie_id"]}', '{movie["title"]}', {movie["year"]}, '{movie["type"]}',
                        {movie["minutes"]}, {movie["rating"]}, {movie["votes"]});
            """
        )

    def delete_movie(self, movie_id: str):
        DatabaseManager().execute_statement(
            f"DELETE FROM usuario WHERE movie_id = {movie_id};"
        )
