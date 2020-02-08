import random
from gen.generators import name, age, gender, sexuality, personality, job, dislikes, likes, skills, hobbies, habits
from gen import c

# insecurities
# priorities

EXPANSION_CONST = 0.5

c.execute("CREATE TABLE persons (id integer primary key, body, name, age, gender, sexuality, job, personality, dislikes, likes, skills, hobbies, habits, partner, friends)")

def produce(args = {}):
    if random.random() < EXPANSION_CONST:
        page = get(args)
        if page:
            return page
    return generate(args)

def get(args = {}):
    text_args = []
    for k,v in args:
        text_args.push("{} = {}".format(k,v))

    print("SELECT * FROM persons WHERE {} ORDER BY RANDOM() LIMIT 1;".format(" AND ".join(text_args)))
    c.execute("SELECT * FROM persons WHERE {} ORDER BY RANDOM() LIMIT 1;".format(" AND ".join(text_args)))
    rows = c.fetchall()
    page = rowToDict(model, rows[0])
    return page

def generate(args = {}):
    person = {}
    person["name"] = args['name'] if "name" in args else name.generate()
    person["age"] = args['age'] if "age" in args else age.generate(25)
    person["gender"] = args['gender'] if "gender" in args else gender.generate()
    person["sexuality"] = args['sexuality'] if "sexulaity" in args else sexuality.generate()
    person["job"] = args['job'] if "job" in args else job.generate()
    person["personality"] = args['personality'] if "personality" in args else personality.generate()
    person["likes"] = args['likes'] if "likes" in args else likes.generate()
    person["dislikes"] = args['dislikes'] if "dislikes" in args else dislikes.generate()
    person["hobbies"] = args['hobbies'] if "hobbies" in args else hobbies.generate()
    person["skills"] = args['skills'] if "skills" in args else skills.generate()

    # set partner constraints
    person["partner"] = args["partner"] if "partner" in args and random.random < 0.3 else produce()["id"]

    # set friendship constraints
    person["friends"] = args["friends"] if "friends" in args else generate_list(produce)

    c.execute("INSERT INTO persons(name, age, gender, sexuality, job, personality, dislikes, likes, skils, hobbies, habits, partner, friends) VALUES()")
    set_reverse_partner(person["id"], person["partner"])

    set_reverse_friendship(person["id"], person["friends"])

def set_reverse_partner(self_id, partner_id):
    c.execute("UPDATE persons SET partner = {} WHERE id = {}".format(self_id, partner_id))

def set_reverse_friendship(self_id, friends_ids):
    for friend_id in friends_ids:
      c.execute("SELECT * FROM persons WHERE id = {}".format(friend_id))
      rows = c.fetchall()
      person = rowToDict(model, rows[0])
      c.execute("UPDATE persons SET friends = {} WHERE id = {}").format("{},{}".format(person.friends, self_id), friend_id)

def generate_list(gen_func, a=3, b=5):
    output_list = []
    for i in range(random.randint(a, b)):
      output_list.push(gen_func()["id"])
    return output_list.join(',')

def pages_to_id(pages):
    return [page["id"] for page in pages]

