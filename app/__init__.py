from flask import Flask
from flask_blitzdb import BlitzDB
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object(__name__)
Bootstrap(app)

db = BlitzDB(app)

from app import views