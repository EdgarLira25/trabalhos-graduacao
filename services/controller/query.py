"""Arquivo na camada de controller intermediando queries e statements"""

from services.database.manager import DatabaseManager


class QueryController:
    """Controller Para as rotas no contexto de query genérica"""

    def __init__(self) -> None:
        pass

    def execute_generic_query(self, query: str) -> str:
        """Repassa a query para o database e formata a query resultante para uma string"""

        query_resp = DatabaseManager().execute_select_all(query)

        if not query_resp:
            return "Resultado Vazio"

        keys = query_resp[0].keys()

        column_lengths = [
            max(len(str(item)) for item in col)
            for col in zip(*[d.values() for d in query_resp] + [keys])
        ]

        def format_row(row):
            return " | ".join(
                f"{str(value).ljust(column_lengths[i])}" for i, value in enumerate(row)
            )

        header = format_row(keys)
        lines = [header, "-" * len(header)]
        for dicionario in query_resp:
            lines.append(format_row(dicionario.values()))

        string = "\n".join(lines)

        return string

    def generic_statement(self, statement: str):
        """Executa statement genérico"""
        DatabaseManager().execute_statement(statement)
