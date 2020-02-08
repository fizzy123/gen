import sqlite3
import importlib
from sqlite3 import Error
from datetime import datetime

# basic setup 
conn = None
try:
    now = datetime.now()
    conn = sqlite3.connect("./{}.db".format(datetime.timestamp(now)))
    print(sqlite3.version)
except Error as e:
    print(e)

c = conn.cursor()

ROOT_MODEL_ID = 'person'
root_model = importlib.import_module("gen.pages.{}".format(ROOT_MODEL_ID))
ROOT_ID = root_model.produce().id

EXPANSION_CONST = 0.5

# web setup
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home_route():
    return page_route(ROOT_MODEL_ID, ROOT_ID)

@app.route('/<model>/<page_id>')
def page_route(model, page_id):
    page = importlib.import_module(model).get({id: page_id})
    return render_template("page.html", page=page)

