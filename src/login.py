from marshmallow_dataclass import dataclass
from src.factory import from_json
from src.user import User

@dataclass
class LoginInfo:
    @staticmethod
    def load():
        return from_json('./data/users/login.json', LoginInfo);

    mail: str
    id: int
    isStudent: bool

def findUserId(email: str):
    logins = LoginInfo.load()
    for login in logins:
        if login.mail == email:
            return login.id
    return -1

def findUser(userId: int):
    return User.load(userId)

def loginUser(email: str, password: str):
    userId = findUserId(email)
    if userId == -1:
        return None
    user = findUser(userId)
    if user.password == password:
        return user
    return None
