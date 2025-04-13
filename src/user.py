from marshmallow_dataclass import dataclass
from src.factory import from_json

@dataclass
class Stats:
    correctAnswers: int

@dataclass
class User:
    @staticmethod
    def load(userId: int):
        return from_json(f'./data/users/students/user_{userId}.json', User);

    name: str
    email: str
    password: str
    stats: Stats
