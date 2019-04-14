import shelve
from flask import Flask, g
from models.User import User
from models.Group import Group

app = Flask(__name__)


def get_db(database):
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = shelve.open(database)
    return db


@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def fill_users():
    shelf = get_db("user.db")

    danius = User(1, "Danius Trumpickas",
                  'https://timebase.lt/media/cache/user_show_small_thumb_retina/uploads/users/2073_f85066f654ba3433775282caa741a5c1526e60ad.jpeg')
    ernesta = User(2, "Ernesta Daugenaite",
                   'https://timebase.lt/media/cache/user_show_small_thumb_retina/uploads/users/3278_39eff5fc59cc56898d2d87df6c70fde746648997.jpeg')
    karolis = User(3, "Karolis Beliasas,",
                      "https://timebase.lt/media/cache/user_small_thumb_retina/uploads/users/3193_fc11859f5695ca877e5560bbc57fdea48ea585f9.jpeg")
    martynasj = User(4, "Martynas Jakimcikas",
                     "https://timebase.lt/media/cache/user_small_thumb_retina/uploads/users/2682_3c7617878dcbb0ba3c5b5426de80fa1644a0c4e7.jpeg")
    martynass = User(5, "Martynas Sileikis",
                     "https://timebase.lt/media/cache/user_show_small_thumb_retina/uploads/users/2867_836fc0bd21babd889e73015e75c2934f0ac358b4.jpeg")
    sarunas = User(6, "Sarunas Kazlauskas",
                   "https://timebase.lt/media/cache/user_show_small_thumb_retina/uploads/users/3265_f6477a7109ed3c1711f72a0e5a987eff823ce712.jpeg")
    alexei = User(7, "Alexei Yakushev",
                  "https://timebase.lt/media/cache/user_show_small_thumb_retina/uploads/users/1553_ee3908ae2cba3f73e2abc85efdf8ccfc42906b81.jpeg")

    if str(danius.id) in shelf:
        return

    shelf[str(danius.id)] = danius
    shelf[str(ernesta.id)] = ernesta
    shelf[str(karolis.id)] = karolis
    shelf[str(martynasj.id)] = martynasj
    shelf[str(martynass.id)] = martynass
    shelf[str(sarunas.id)] = sarunas
    shelf[str(alexei.id)] = alexei


def fill_groups():
    shelf = get_db("group.db")

    floor6 = Group(101, 'Mediapark  - 6th floor (25)')
    partners = Group(102, 'Mediapark HCK (101)')

    if str(floor6.id) in shelf:
        return

    shelf[str(floor6.id)] = floor6
    shelf[str(partners.id)] = partners
