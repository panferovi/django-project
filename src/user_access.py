from dataclasses import dataclass
from src.factory import from_json, to_json
from src.user import User

LOGINS='./data/users/login.json'

@dataclass
class LoginInfo:
    def __init__(self, email: str, userId: int, isStudent: bool):
        self.email = email
        self.userId = userId
        self.isStudent = isStudent

    @staticmethod
    def load():
        return from_json(LOGINS, LoginInfo);

    @staticmethod
    def store(email: str):
        logins = LoginInfo.load()
        print(f'LoginInfo.load() {logins}')
        userId = len(logins)
        logins.append(LoginInfo(email, userId, True))
        print(logins)
        to_json(LOGINS, logins)
        return userId

    email: str
    userId: int
    isStudent: bool

def findUserId(email: str):
    logins = LoginInfo.load()
    print(f'logins: {logins}')
    for login in logins:
        if login.email == email:
            return login.userId
    return -1

def findUser(userId: int):
    return User.load(userId)

def loginUser(email: str, password: str):
    print("loginUser")
    userId = findUserId(email)
    print(f"userId: {userId}")
    if userId == -1:
        return None
    print('before findUser')
    user = findUser(userId)
    print(f'findUser: {user}')
    if user.password == password:
        return user
    return None

def createUser(name: str, email: str, password: str):
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    userId = LoginInfo.store(email)
    print(userId)
    return User.store(userId, name, email, password)

def registerUser(name: str, email: str, password: str):
    userId = findUserId(email)
    if userId == -1:
        return createUser(name, email, password)
    return None
