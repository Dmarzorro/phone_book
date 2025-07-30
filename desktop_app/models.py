from peewee import *
from datetime import datetime
from uuid import uuid4

db = SqliteDatabase('contactlist.db')

class Contact(Model):
    id = UUIDField(primary_key=True, default=uuid4)
    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)
    phone = CharField(unique=True)
    email = CharField(null=True, unique=True)
    created_at = DateTimeField(default=datetime.now)

    def __str__(self) -> str:
        email_display = self.email or "No Email"
        return f"{self.first_name} {self.last_name} {self.phone} {email_display}"

    class Meta:
        database = db
        table_name = 'contacts'
