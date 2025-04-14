from dataclasses import dataclass
from src.factory import from_json, to_json
from copy import deepcopy

@dataclass
class TopicStats:
    def __init__(self, total=0, correct=0):
        self.total = total
        self.correct = correct

    @property
    def percent(self):
        if self.total == 0:
            return 0
        return self.correct * 100 / self.total

    total: int
    correct: int

@dataclass
class Stats:
    def __init__(self, total=0, correct=0, addition=TopicStats(),
                                           subtraction=TopicStats(),
                                           comparison=TopicStats(),
                                           logic=TopicStats(),
                                           time=TopicStats(),
                                           money=TopicStats()):
        self.total = total
        self.correct = correct
        self.addition = addition
        self.subtraction = subtraction
        self.comparison = comparison
        self.logic = logic
        self.time = time
        self.money = money

    def update_stats(self, isCorrect, topic):
        topicObj = getattr(self, topic)
        self.total += 1
        topicObj.total += 1
        if isCorrect:
            self.correct += 1
            topicObj.correct += 1
        setattr(self, topic, topicObj)

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
    def __init__(self, userId, name, email, password, stats):
        self.userId = userId
        self.name = name
        self.email = email
        self.password = password
        self.stats = stats

    @staticmethod
    def load(userId: int):
        return from_json(f"./data/users/students/user_{userId}.json", User);

    @staticmethod
    def store(user):
        to_json(f'./data/users/students/user_{user.userId}.json', user)

    def get_stats(self):
        return self.stats

    def update_stats(self, isCorrect, topic):
        self.stats.update_stats(isCorrect, topic)

    userId: int
    name: str
    email: str
    password: str
    stats: Stats
