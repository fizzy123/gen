import random

genders = [
    "male",
    "female",
    "nonbinary"
]

def generate():
    return random.choices(genders, [10,10,1])