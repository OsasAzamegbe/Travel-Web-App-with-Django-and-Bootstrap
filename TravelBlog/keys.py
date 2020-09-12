import environ

env = environ.Env()

environ.Env.read_env()

SETTINGS_SECRET_KEY = env('SETTINGS_SECRET_KEY')