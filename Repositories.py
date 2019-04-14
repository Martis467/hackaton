import shelve
from flask import Flask, g
from models.User import User

app = Flask(__name__)


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = shelve.open("users.db")
    return db


@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def fill_users():
    shelf = get_db()

    danius = User(1, "Danius Trumpickas", 'https://timebase.lt/media/cache/user_show_small_thumb_retina/uploads/users/2073_f85066f654ba3433775282caa741a5c1526e60ad.jpeg')
    ernesta = User(2, "Ernesta Daugenaite", 'https://timebase.lt/media/cache/user_show_small_thumb_retina/uploads/users/3278_39eff5fc59cc56898d2d87df6c70fde746648997.jpeg')

    shelf[str(danius.id)] = danius
    shelf[str(ernesta.id)] = ernesta