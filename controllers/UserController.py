from flask import Flask, g
from flask_restful import Resource
from Repositories import get_db

app = Flask(__name__)


class UserController(Resource):
    def get(self):
        shelf = get_db()
        keys = list(shelf.keys())

        users = []

        for key in keys:
            users.append(convert_to_json(shelf[key]))

        return {'message': 'Success', 'data': users}, 200


def convert_to_json(user):
    return {'id': user.id,
            'fullName': user.full_name,
            'photoUrl': user.photo_url}
