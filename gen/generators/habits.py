import random

habits = [
    "lies for fun",
    "vegetarian",
    "vegan",
    "always on some diet",
    "always listening to music",
    "wears glasses",
    "wears contacts",
    "germaphobic",
    "falls asleep easily",
    "has lots of trouble falling asleep",
    "picky eater",
    "night owl",
    "morning person",
    "scavenger",
    "doesn't call things what they're actually called",
    "frequently sick",
    "always cold",
    "never cold",
    "always drumming",
    "sings a lot",
    "whistles",
    "quoting movies and shit",
    "always has a water bottle",
    "frequently forgets to bring things",
    "loses stuff often",
    "has piercings",
    "has tattoo(s)",
    "snacks often",
    "owns a pet",
    "works out"
]

def generate():
    return random.sample(habits, random.randint(3,5)).join(', ')
