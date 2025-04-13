from marshmallow_dataclass import dataclass
from factory import from_json

@dataclass
class LoginInfo:
    @staticmethod
    def create():
        return from_json('./data/users/login.json', LoginInfo);

    mail: str
    id: int
    isStudent: bool
