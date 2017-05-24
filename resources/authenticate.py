from flask import jsonify, Blueprint, session

from flask_restful import Resource, Api, fields, reqparse, abort

import boto

instance_fields = {
    'aws_access_key_id': fields.String,
    'aws_secret_access_key': fields.String
}


class Authenticate(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument(
            'aws_access_key_id',
            required=True,
            help="No access key provided.",
            location=['form', 'json']
        ),
        self.parser.add_argument(
            'aws_secret_access_key',
            required=True,
            help="No secret key provided.",
            location=['form', 'json']
        )

    def post(self):
        args = self.parser.parse_args()
        try:
            client = boto.connect_ec2(
                aws_access_key_id=args['aws_access_key_id'],
                aws_secret_access_key=args['aws_secret_access_key'])
            client.get_all_reservations()

        except:
            abort(404, message="Please provide valid keys.")
        else:
            session['key'] = args
            return jsonify({'session': session['key']})


authenticate_api = Blueprint('resources.authenticate', __name__)
api = Api(authenticate_api)
api.add_resource(Authenticate, '/authenticate', endpoint="authenticate")
