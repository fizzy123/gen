from itertools import combinations

personality_traits = [
    ["inventive", "curious", "consistent", "cautious"],
    ["efficient", "organized", "easy-going", "careless"],
    ["outgoing", "energetic", "solitary", "reserved"],
    ["friendly", "compassionate", "detatched", "confrontational"],
    ["sensitive", "nervous", "secure", "confident"]
]

def generate():
    combination = combinations(personality_traits, 3)
    personality_list = []
    for trait in combination:
        personality_list.push(random.choice(trait))
    return personality_list.join(', ')
