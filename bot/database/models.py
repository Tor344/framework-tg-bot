from tortoise import fields
from tortoise.models import Model

class User(Model):
    id = fields.IntField(pk=True)
    user_name = fields.TextField()
    age = fields.IntField()