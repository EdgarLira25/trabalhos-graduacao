from typing import NamedTuple


# Para um projeto universitário talvez não seja necessário criar os models para o database
class User(NamedTuple):
    nome: str
    senha: str
