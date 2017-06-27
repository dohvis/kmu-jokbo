from datetime import datetime
from app import (
    db,
)


class Exam(db.Document):
    key = db.StringField(required=True, max_length=128)
    subject = db.StringField(required=True)
    professor = db.StringField(required=True, max_length=16)
    year = db.IntField()
    semester = db.StringField(required=True, max_length=2)
    case = db.StringField(required=True, max_length=2)

    file_format = db.StringField(required=True, max_length=32)
    created_at = db.DateTimeField(default=datetime.now())
