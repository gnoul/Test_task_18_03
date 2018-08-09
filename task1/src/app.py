from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
app.db = SQLAlchemy(app)

from users import views
from users import models


@app.before_first_request
def populatedb():
    _hash = models.user_manager.hash_password('QWEqwe123')
    tablename = models.User.__tablename__
    username = 'admin'
    q = f"""INSERT INTO "{tablename}" (username, password, is_staff, active) 
            VALUES ('{username}', '{_hash}', true, true) 
            ON CONFLICT(username) DO NOTHING;"""
    connection = app.db.session.connection()
    connection.execute(q)
    app.db.session.commit()


if __name__ == '__main__':
    app.run()
