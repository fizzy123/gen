import random
jobs = [
  "Architect",
  "Construction Laborer",
  "Electrician",
  "Environmental Engineer",
  "Janitor",
  "Mechanical Engineer",
  "Plumber"
]

def generate():
    return random.choices(jobs)