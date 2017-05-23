from flask import jsonify, Blueprint, request, Response

from flask_restful import Resource, Api, reqparse

from utils import get_instances

import json


class InstanceList(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('session_id', location='cookies')

    def get(self):
        args = request.headers.get('userInfo')
        aws_keys = json.loads(args)

        instances = get_instances(aws_keys['aws_access_key_id'], aws_keys['aws_secret_access_key'])
        return jsonify({"data": instances})


instances_api = Blueprint('resources.instances', __name__)
api = Api(instances_api)
api.add_resource(InstanceList, '/instances', endpoint="instances")
