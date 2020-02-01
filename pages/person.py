from ../generators import name, age, gender, sexuality, personality, job
from ./ import quirks, skills, hobbies, habits, aesthetic

c.execute("""CREATE TABLE persons (id integer primary key, body, name, age, gender, sexuality, job, personality, quirks, skills, hobbies, partner, friends, insecurities, priorities)""")

def produce(args):
    if random.random() < EXPANSION_CONST:
        page = get(args)
        if page:
            return page
    return generate(args)

def get(args):
    text_args = []
    for k,v in args:
        text_args.push("{} = {}".format(k,v))

    c.execute("""SELECT * FROM {} WHERE {} ORDER BY RANDOM() LIMIT 1;""".format(text_args.join(' AND ')))
    rows = c.fetchall()
    page = rowToDict(model, rows[0])
    return page

def generate(args):
    person = {}
    person.name = args.name if args.name else name.generate()
    person.age = args.age if args.age else age.generate(25)
    person.gender = args.gender if args.gender else gender.generate()
    person.sexuality = args.sexuality if args.sexuality else sexuality.generate()
    person.job = args.job if args.job else job.generate()
    person.personality = args.personality if args.personality else personality.generate
    person.quirks = args.quirks if args.quirks else generate_list(quirks.generate)
    person.hobbies = args.hobbies if args.hobbies else pages_to_id(generate_list(hobbies.generate))
    person.skills = args.skills if args.skills else pages_to_id(generate_list(skills.generate))

    # set partner constraints
    person.partner = args.partner if args.partner else produce().id

    # set friendship constraints
    person.friends = args.friends if args.friends else generate_list(produce)

    c.execute("""INSERT INTO persons(name, age, gender, sexuality, job, personality, quirks, skils, hobbies, partner, friends) VALUES()

"""
    setReversePartner(person.id, person.partner)

    setReverseFriendship(person.id, person.friends)

def setReversePartner(self_id, partner_id):
    c.execute("""UPDATE persons SET partner = {} WHERE id = {}""".format(self_id, partner_id))

def setReverseFriendship(self_id, friends_ids):
    for friend_id in friends_ids:
      c.execute("""SELECT * FROM persons WHERE id = {}""".format(friend_id))
      rows = c.fetchall()
      person = rowToDict(model, rows[0])
      c.execute("""UPDATE persons SET friends = {} WHERE id = {}""".format("{},{}".format(person.friends, self_id), friend_id)

def generate_list(gen_func, a=3, b=5):
    output_list = []
    for i in range(random.randint(a, b)):
      output_list.push(gen_func().id)
    return output_list.join(',')

def pages_to_id(pages):
    return [page.id for page in pages]

def instantiate():