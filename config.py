import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


def get_env(var):
    return os.environ[var]

SECRET_KEY = get_env('SECRET_KEY')
MONGODB_DB = get_env('MONGODB_DB')
MONGODB_HOST = get_env('MONGODB_HOST')
MONGODB_PORT = int(get_env('MONGODB_PORT'))
MONGODB_USERNAME = get_env('MONGODB_USERNAME')
MONGODB_PASSWORD = get_env('MONGODB_PASSWORD')

AWS_ACCESS_KEY_ID = get_env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = get_env('AWS_SECRET_ACCESS_KEY')
AWS_S3_BUCKET_NAME = get_env('AWS_S3_BUCKET_NAME')
