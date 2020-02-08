import random

dislikes = [
    "popular stuff",
    "coffee",
    "being woken up",
    "loud noises",
    "repetitive noises",
    "dogs",
    "cats",
    "phone calls",
    "insects"
]

def generate():
    return random.sample(dislikes, random.randint(1, 5)).join(", ")
