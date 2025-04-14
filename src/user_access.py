from dataclasses import dataclass
from src.factory import from_json, to_json
from src.user import User, Stats

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
        userId = len(logins)
        logins.append(LoginInfo(email, userId, True))
        to_json(LOGINS, logins)
        return userId

    email: str
    userId: int
    isStudent: bool

def findUserId(email: str):
    logins = LoginInfo.load()
    for login in logins:
        if login.email == email:
            return login.userId
    return -1

def findUser(userId: int):
    return User.load(userId)

def createUser(name: str, email: str, password: str):
    userId = LoginInfo.store(email)
    ActiveUser.store(userId)
    user = User(userId, name, email, password, Stats())
    User.store(user)
    return user

def loginUser(email: str, password: str):
    userId = findUserId(email)
    if userId == -1:
        return None
    user = findUser(userId)
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

def getActiveStats():
    activeUser = ActiveUser.load()
    user = findUser(activeUser.userId)
    return user.get_stats()

def updateActiveStats(isCorrect: bool, topic: str):

    activeUser = ActiveUser.load()
    user = findUser(activeUser.userId)
    user.update_stats(isCorrect, topic)
    User.store(user)
    return user.get_stats()
