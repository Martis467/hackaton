from flask_restful import Resource
from repository.DatabaseManager import querry_database, insert_to_database, get_top
from models.User import User
import random


class RandomGameController(Resource):
    def post(self, index):
        sql = ''' INSERT INTO Game(GroupId) VALUES(?)'''
        task = (index,)
        id = insert_to_database(sql, task)

        return {'message': 'Success', 'data': id}, 200

    def get(self, index):
        top_game = self.get_game(index)
        group_id = top_game[1]
        users = self.get_users()

        user = users[0]

        if group_id == 1:
            game_users = users[0:3]
            randomWinner = random.randint(1, len(game_users))
            user = game_users[randomWinner-1]
        else:
            game_users = users[3:]
            randomWinner = random.randint(1, len(game_users))
            user = game_users[randomWinner-1]


        data = {'id': user.id,
                'fullName': user.full_name,
                'photoUrl': user.photo_url}

        return {'message': 'Success', 'data': data}, 200

    def get_game(self, index):
        top_game = querry_database('SELECT * FROM Game')
        return top_game[index-1]


    def get_users(self):
        user_result = querry_database('SELECT * FROM User')

        users = []

        for row in user_result:
            user = User(row)
            users.append(user)

        return users