"""Module allows to register and login user"""

from dataclasses import dataclass
from src.factory import from_json, to_json
from src.user import User, Stats

LOGINS = "./data/users/login.json"
ACTIVE_USER = "./data/users/active_user.json"


@dataclass
class ActiveUser:
    def __init__(self, user_id: int):
        self.user_id = user_id

    @staticmethod
    def load():
        """Function loads active user from the server"""
        return from_json(ACTIVE_USER, ActiveUser)

    @staticmethod
    def store(user_id: int):
        """Function stores active user on the server"""
        active_user = ActiveUser(user_id)
        return to_json(ACTIVE_USER, active_user)

    user_id: int


@dataclass
class LoginInfo:
    def __init__(self, email: str, user_id: int, is_student: bool):
        self.email = email
        self.user_id = user_id
        self.is_student = is_student

    @staticmethod
    def load():
        """Function loads array of registered users from the server"""
        return from_json(LOGINS, LoginInfo)

    @staticmethod
    def store(email: str):
        """Function appends user registered users and store to the server"""
        logins = LoginInfo.load()
        user_id = len(logins)
        logins.append(LoginInfo(email, user_id, True))
        to_json(LOGINS, logins)
        return user_id

    email: str
    user_id: int
    is_student: bool


def find_user_id(email: str):
    """Function finds user_id by email"""
    logins = LoginInfo.load()
    for login in logins:
        if login.email == email:
            return login.user_id
    return -1


def find_user(user_id: int):
    """Function loads user by user_id"""
    return User.load(user_id)


def create_user(name: str, email: str, password: str):
    """Function creates new user with name, email and password"""
    user_id = LoginInfo.store(email)
    ActiveUser.store(user_id)
    user = User(user_id, name, email, password, Stats())
    User.store(user)
    return user


def login_user(email: str, password: str):
    """Function tries to login user"""
    user_id = find_user_id(email)
    if user_id == -1:
        return None
    user = find_user(user_id)
    if user.password == password:
        ActiveUser.store(user_id)
        return user
    return None


def register_user(name: str, email: str, password: str):
    """Function tries to register user"""
    user_id = find_user_id(email)
    if user_id == -1:
        return create_user(name, email, password)
    return None


def get_active_user():
    """Function returns active user"""
    active_user = ActiveUser.load()
    return find_user(active_user.user_id)


def get_active_stats():
    """Function returns stats of active user"""
    user = get_active_user()
    return user.get_stats()


def update_active_stats(is_correct: bool, topic: str):
    """Function updates stats of active user"""
    user = get_active_user()
    user.update_stats(is_correct, topic)
    User.store(user)
    return user.get_stats()
