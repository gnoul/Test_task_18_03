from flask_user import UserManager, UserMixin
from app import app

db = app.db


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    active = db.Column('active', db.Boolean(), nullable=False, server_default='0')
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False, server_default='')
    is_staff = db.Column('is_staff', db.Boolean(), nullable=False, server_default='0')

    def __repr__(self):
        return '<User {}>'.format(self.username)


db.create_all()
user_manager = UserManager(app, db, User)
