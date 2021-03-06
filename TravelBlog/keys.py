import environ

env = environ.Env()

environ.Env.read_env()

SETTINGS_SECRET_KEY = env('SETTINGS_SECRET_KEY')

DB_USERNAME = env('DB_USERNAME')
DB_PASSWORD = env('DB_PASSWORD')

AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')