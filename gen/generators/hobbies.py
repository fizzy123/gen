import random

hobbies = [
  "drawing",
  "working out",
  "running",
  "hiking",
  "videao games",
  "making stuff",
  "programming",
  "hosting events",
  "cooking",
  "sewing",
  "baking",
  "biking",
  "beer",
  "movies",
  "tv shows",
]

def generate():
    return random.sample(hobbies, random.randint(1, 5)).join(', ')
