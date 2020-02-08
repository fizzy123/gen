skills = [
  "cooking",
  "knittiing",
  "computers",
  "wood working",
  "home improvement",
  "interior design",
  "graphic design",
  "programming",
  "drawing",
  "mixology",
  "cleaning",
  "planning/organizing",
  "writing",
  "hosting",
  "making new friends"
]

def generate():
    return random.sample(skills, random.randint(1, 10)).join(', ')
