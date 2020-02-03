from app import db
import datetime

class User(db.Document):
    Username = db.StringField(max_length=64)
    Password = db.StringField(max_length=120)
    FirstName = db.StringField(max_length=120)
    LastName = db.StringField(max_length=120)
    MiddleName = db.StringField(max_length=120)
    created = db.DateTimeField(default=datetime.datetime.utcnow())

    def __repr__(self):
        return '<User %r>' %(self.firstname)
