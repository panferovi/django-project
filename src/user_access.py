from dataclasses import dataclass
from src.factory import from_json, to_json
from src.user import User

LOGINS='./data/users/login.json'
ACTIVE_USER='./data/users/active_user.json'

@dataclass
class ActiveUser:
    def __init__(self, userId: int):
        self.userId = userId

    @staticmethod
    def load():
        return from_json(ACTIVE_USER, ActiveUser);

    @staticmethod
    def store(userId: int):
        activeUser = ActiveUser(userId);
        return to_json(ACTIVE_USER, activeUser);

    userId: int

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

def createUser(name: str, email: str, password: str):
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    userId = LoginInfo.store(email)
    print(userId)
    ActiveUser.store(userId)
    return User.store(userId, name, email, password)

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
        ActiveUser.store(userId)
        return user
    return None

def registerUser(name: str, email: str, password: str):
    userId = findUserId(email)
    if userId == -1:
        return createUser(name, email, password)
    return None

def getActiveUser():
    activeUser = ActiveUser.load()
    return findUser(activeUser.userId)