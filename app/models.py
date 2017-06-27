from datetime import datetime
from app import (
    db,
)


class Exam(db.Document):
    key = db.StringField(required=True, max_length=32)
    subject = db.StringField(required=True)
    professor = db.StringField(required=True, max_length=16)
    year = db.IntField()
    period = db.StringField(required=True, max_length=2)
    case = db.StringField(required=True, max_length=2)

    file_format = db.StringField(required=True, max_length=16)
    created_at = db.DateTimeField(default=datetime.now())
