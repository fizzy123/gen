import random

priorities = [
    "friends",
    "family",
    "career",
    "money",
    "reputation",
    "public perception",
    "justice",
    "entertainment",
    "power",
    "comfort",
    "morality",
    "empathy",
    "appearance"
]

def generate():
    return random.sample(priorities, likes, random.randint(1,3))
