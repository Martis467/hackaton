from flask_restful import Resource
from repository.DatabaseManager import querry_database, insert_to_database


class RandomGameController(Resource):
    def post(self, index):
        sql = ''' INSERT INTO Game(GroupId) VALUES(?)'''
        task = (index,)
        insert_to_database(sql, task)

    def get(self, index):
        return
