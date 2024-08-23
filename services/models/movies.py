from typing import TypedDict


class Movies(TypedDict):
    movie_id: str
    title: str
    year: int
    type: str
    minutes: int
    rating: float
    votes: int
