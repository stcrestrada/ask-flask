from flask import jsonify, Blueprint, request

from flask_restful import Resource, Api, reqparse

from utils import get_instances

from peewee import IntegrityError

from models import Instance, DATABASE

import json


class InstanceList(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('userInfo', required=True, help="Please provide aws access key and secret key.",
                                 location='headers')

    def get(self):
        args = request.headers.get('userInfo')
        aws_keys = json.loads(args)

        instances = get_instances(aws_keys['aws_access_key_id'], aws_keys['aws_secret_access_key'])
        for i in instances:
            instance_id = i.get('instance_id')
            availability_zone = i.get('availability_zone')
            instance_state = i.get('instance_state')
            try:
                with DATABASE.atomic():
                    Instance.create(instance_id=instance_id)

            except IntegrityError:
                pass
        return jsonify({"data": instances})

    def post(self):
        pass


instances_api = Blueprint('resources.instances', __name__)
api = Api(instances_api)
api.add_resource(InstanceList, '/instances', endpoint="instances")
