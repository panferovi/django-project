from dataclasses import dataclass
from src.factory import from_json, to_json

@dataclass
class Stats:
    correct_answers: int = 0

@dataclass
class User:
    def __init__(self, name, email, password, stats):
        self.name = name
        self.email = email
        self.password = password
        self.stats = stats

    @staticmethod
    def load(userId: int):
        return from_json(f"./data/users/students/user_{userId}.json", User);

    @staticmethod
    def store(userId: int, name: str, email: str, password: str):
        user = User(name, email, password, Stats())
        to_json(f'./data/users/students/user_{userId}.json', user)
        return user

    name: str
    email: str
    password: str
    stats: Stats
