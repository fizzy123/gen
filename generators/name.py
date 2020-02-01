from faker import Faker
fake = Faker()

def generate():
    return fake.name()