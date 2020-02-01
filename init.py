import sqlite3
from sqlite3 import Error
from datetime import datetime

import pages

# basic setup 
conn = None
try:
    conn = sqlite3.connect("./{}.db".format(datetime.timestamp()))
    print(sqlite3.version)
except Error as e:
    print(e)
finally:
    if conn:
        conn.close()

c = conn.cursor()

ROOT_MODEL_ID = 'person'
root_model = importlib.import_module(ROOT_MODEL_ID)
ROOT_ID = rootModel.produce().id

EXPANSION_CONST = 0.5

# web setup
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home_route():
    return page_route(ROOT_MODEL_ID, ROOT_ID))

@app.route('/<model>/<page_id>')
def page_route(model. page_id):
    page = importlib.import_module(model).get({id: page_id})
    return render_template("page.html", page=page)

