import datetime

from peewee import *

DATABASE = SqliteDatabase('instances.sqlite')


class Instance(Model):
    instance_id = CharField(unique=True)
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Instance], safe=True)
    DATABASE.close()
