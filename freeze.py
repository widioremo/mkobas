#!venv/bin/python
from flask_frozen import Freezer
from app import app

freezer = Freezer(app)
app.testing = True

if __name__ == '__main__':

    freezer.freeze()