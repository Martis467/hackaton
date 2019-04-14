from flask_restful import Resource
from repository.DatabaseManager import querry_database
from models.Group import Group
from models.User import User


class GroupController(Resource):
    def get(self):
        group_result = self.get_groups()
        user_result = self.get_users()

        grouped_users = []

        grouped_user1 = convert_to_json(group_result[0], user_result[0:3])
        grouped_user2 = convert_to_json(group_result[1], user_result[3:])

        grouped_users.append(grouped_user1)
        grouped_users.append(grouped_user2)

        return {'message': 'Success', 'data': grouped_users}, 200

    def get_groups(self):
        group_result = querry_database('SELECT * FROM Groupings')

        groups = []

        for grp in group_result:
            group = Group(grp)
            groups.append(group)

        return groups

    def get_users(self):
        user_result = querry_database('SELECT * FROM User')

        users = []

        for row in user_result:
            user = User(row)
            users.append(user)

        return users


def convert_to_json(group, users):
    return {'id': group.id,
            'name': group.name,
            'users': get_user_dict(users)}


def get_user_dict(users):
    user_array = []

    for user in users:
        user_dict = {'id': user.id,
         'fullName': user.full_name,
         'photoUrl': user.photo_url}
        user_array.append(user_dict)

    return user_array
