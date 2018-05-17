from flask import Flask
from flask_restful import Resource, Api, reqparse

## Import and instantiate custom stuff
from config import Config
from utils.timestamp import Timestamp
config = Config()
timestamp = Timestamp()

## Instantiate the Flask stuff
app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()

## Our non-pretty reply contents stored global
REPLY_CONTENTS = {
            'doorOpen': None,
            'lastDoorMeasurement': None,
            'lastDoorChange': None,
            'lastInsideChange': None,
            'lastInsideValue': None
        }

class Main(Resource):
    def __init__(self):
        pass

    def get(self):
        return REPLY_CONTENTS

class Update(Resource):
    def __init__(self):
        parser.add_argument('name')
        parser.add_argument('data')
        parser.add_argument('coreid')
        parser.add_argument('published_at')

    def post(self):
        args = parser.parse_args(strict=True)
        print(args)
        return 'OK'
        
api.add_resource(Update, '/update')
api.add_resource(Main, '/')

if __name__ == '__main__':
    app.run(debug=True)