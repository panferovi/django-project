"""Module represents user class and api to work with"""

from dataclasses import dataclass
from src.factory import from_json, to_json

@dataclass
class TopicStats:
    def __init__(self, total=0, correct=0):
        self.total = total
        self.correct = correct

    total: int
    correct: int

@dataclass
class Stats:
    def __init__(
        self,
        total=0,
        correct=0,
        addition=TopicStats(),
        subtraction=TopicStats(),
        comparison=TopicStats(),
        logic=TopicStats(),
        time=TopicStats(),
        money=TopicStats(),
    ):
        self.total = total
        self.correct = correct
        self.addition = addition
        self.subtraction = subtraction
        self.comparison = comparison
        self.logic = logic
        self.time = time
        self.money = money

    def update_stats(self, is_correct, topic):
        """Function updates global and topic stats"""
        topic_obj = getattr(self, topic)
        self.total += 1
        topic_obj.total += 1
        if is_correct:
            self.correct += 1
            topic_obj.correct += 1
        setattr(self, topic, topic_obj)

    total: int
    correct: int
    addition: TopicStats
    subtraction: TopicStats
    comparison: TopicStats
    logic: TopicStats
    time: TopicStats
    money: TopicStats

@dataclass
class User:
    def __init__(self, user_id, name, email, password, stats):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.stats = stats

    @staticmethod
    def load(user_id: int):
        """Function loads user from the server"""
        return from_json(f"./data/users/students/user_{user_id}.json", User)

    @staticmethod
    def store(user):
        """Function stores user on the server"""
        to_json(f"./data/users/students/user_{user.user_id}.json", user)

    def get_stats(self):
        """Function returns stats of user"""
        return self.stats

    def update_stats(self, is_correct, topic):
        """Function updates stats of user"""
        self.stats.update_stats(is_correct, topic)

    user_id: int
    name: str
    email: str
    password: str
    stats: Stats
