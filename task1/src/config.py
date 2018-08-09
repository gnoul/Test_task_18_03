from os import environ as env

DEBUG = env.get('DEBUG') == 'True'

# Flask-User settings
USER_ENABLE_EMAIL = False  # Disable email authentication
USER_ENABLE_USERNAME = True  # Enable username authentication
USER_REQUIRE_RETYPE_PASSWORD = False  # Simplify register form

SECRET_KEY = 'WARNING: Flask-User TokenManager: SECRET_KEY is shorter than 32 bytes.'

POSTGRES_USER = env.get('POSTGRES_USER', 'pguser1')
POSTGRES_DB = env.get('POSTGRES_DB', 'pddb1')
POSTGRES_PASSWORD = env.get('POSTGRES_PASSWORD', 'ohd7ua2Quu')
POSTGRES_HOST = env.get('POSTGRES_HOST', 'db')
POSTGRES_PORT = env.get('POSTGRES_PORT', 5432)
SQLALCHEMY_DATABASE_URI = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@' \
                          f'{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = False  # Avoids SQLAlchemy warning

USER_LOGIN_URL = '/login'
USER_LOGOUT_URL = '/logout'
USER_REGISTER_URL = '/register'
