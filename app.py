from flask import Flask
from flask_restful import Api
from controllers.GroupController import GroupController
from controllers.UserController import UserController

app = Flask(__name__)


app = Flask(__name__)
api = Api(app)

database = "randomizer.db"


@app.route('/')
def index():
    return "Hello world"


api.add_resource(UserController, '/users')
api.add_resource(GroupController, '/groups')


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)

