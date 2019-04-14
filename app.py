from flask import Flask
from flask_restful import Api
from Repositories import fill_users
from controllers.UserController import UserController

app = Flask(__name__)


app = Flask(__name__)
api = Api(app)


@app.route('/')
def index():
    fill_users()
    return "Hello world"


api.add_resource(UserController, '/users')


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)

