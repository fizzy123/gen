import random

likes = [
  "music",
  "cute things",
  "video games",
  "movies",
  "tv shows",
  "nature",
  "dogs",
  "cats",
  "animals"
  "spicy food",
  "sweet food",
  "meat",
  "drinking",
  "weed",
  "vaping"
  "smoking",
  "drugs",
  "coffee",
  "bubble tea",
  "deals",
  "fashion",
  "reading",
  "politics",
  "good smells",
  "tea",
  "cooking",
  "rain",
  "parties"
]

def generate():
    return random.sample(likes, random.randint(1, 5)).join(", ")
