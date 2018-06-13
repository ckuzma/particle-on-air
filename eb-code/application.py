from flask import Flask
from flask_restful import Resource, Api, reqparse

## Instantiate the Flask stuff
application = app = Flask(__name__) # Formatted for EB
api = Api(app)
parser = reqparse.RequestParser()

## Our non-pretty reply contents stored global
REPLY_CONTENTS = {
            'doorOpen': None,
            'lastDoorMeasurement': None,
            'lastDoorChange': None,
            'lastInsideChange': None,
        }

class Main(Resource):
    def get(self):
        return REPLY_CONTENTS

class Update(Resource):
    def __init__(self):
        parser.add_argument('event')
        parser.add_argument('data')
        parser.add_argument('published_at')
        parser.add_argument('coreid')
        pass

    def post(self):
        args = parser.parse_args()
        print(args)
        self.update_status(args)
        return 'OK'

    def update_status(self, args):
        if args['event'] == 'distance-inch':
            door_open = None
            if float(args['data']) > 4.0:
                door_open = True
            else:
                door_open = False
            if REPLY_CONTENTS['doorOpen'] != door_open:
                REPLY_CONTENTS['lastDoorChange'] = args['published_at']
            REPLY_CONTENTS['doorOpen'] = door_open
            REPLY_CONTENTS['lastDoorMeasurement'] = args['published_at']
        if args['event'] == 'pir-sensor':
            REPLY_CONTENTS['lastInsideChange'] = args['published_at']
        
api.add_resource(Update, '/update')
api.add_resource(Main, '/')

if __name__ == '__main__':
    app.run(debug=True)