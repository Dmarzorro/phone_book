from peewee import *
from datetime import datetime

db = SqliteDatabase('contactlist.db')

class BaseModel(Model):
    class Meta:
        database = db

class Contact(Model):
    id = UUIDField(primary_key=True, default=uuid4)
    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)
    phone = CharField(unique=True)
    email = CharField(null=True, unique=True)
    created_at = DateTimeField(default=datetime.now)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        table_name = 'contacts'

