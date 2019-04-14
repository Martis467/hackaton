from flask_restful import Resource
from Repositories import get_db
from repository.DatabaseManager import querry_database


class GroupController(Resource):
    def get(self):
        shelf = self.get_groups()

        keys = list(shelf.keys())

        groups = []

        for key in keys:
            groups.append(convert_to_json(shelf[key]))

        return {'message': 'Success', 'data': groups}, 200

    def get_groups(self):
        user_result = querry_database('SELECT * FROM User')

        users = []

        for row in user_result:
            user = User(row)
            users.append(user)

        return users


def convert_to_json(group):
    return {'id': group.id,
            'name': group.name}
