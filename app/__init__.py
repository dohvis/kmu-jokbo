from boto3.session import Session
from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__, template_folder='templates')
app.debug = True
app.config.from_object('config')

aws_session = Session(
    aws_access_key_id=app.config.get('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=app.config.get('AWS_SECRET_ACCESS_KEY'),
    region_name='ap-northeast-2',
)

db = MongoEngine()
db.init_app(app)

from app.models import *  # NOQA
from app.controllers import *  # NOQA
