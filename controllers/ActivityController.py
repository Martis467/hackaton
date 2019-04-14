from flask_restful import Resource, reqparse
from repository.DatabaseManager import querry_database, insert_to_database
from models.Activity import Activity


class ActivityController(Resource):
    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('name', required=True)
        parser.add_argument('date', required=True)

        args = parser.parse_args()

        self.post_activity(args['name'], args['date'])

        return {'message': 'Success'}, 200

    def post_activity(self, name, date):
        sql = ''' INSERT INTO Activity(Name, DateCreated) VALUES(?,?) '''
        task = (name, date)
        insert_to_database(sql, task)

    def get(self):
        activity_result = self.get_activity()

        activities = []

        for activity in activity_result:
            activities.append(convert_to_json(activity))

        return {'message': 'Success', 'data': activities}, 200

    def get_activity(self):
        activity_result = querry_database('SELECT * FROM Activity')

        activities = []

        for row in activity_result:
            activity = Activity(row)
            activities.append(activity)

        return activities


def convert_to_json(activity):
    return {'id': activity.id,
            'name': activity.name,
            'date': activity.date}
