from flask_restful import Resource
from repository.DatabaseManager import querry_database
from models.User import User


class UserController(Resource):
    def get(self):
        user_result = self.get_users()

        users = []

        for user in user_result:
            users.append(convert_to_json(user))

        return {'message': 'Success', 'data': users}, 200

    def get_users(self):
        user_result = querry_database('SELECT * FROM User')

        users = []

        for row in user_result:
            user = User(row)
            users.append(user)

        return users


def convert_to_json(user):
    return {'id': user.id,
            'fullName': user.full_name,
            'photoUrl': user.photo_url}
