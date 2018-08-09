from sqlalchemy import exc

from flask import flash, jsonify, render_template, request, send_from_directory
from flask_user import login_required
from flask_login import current_user

from app import app
from .models import user_manager, User


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/users')
@login_required
def users():
    usersqs = app.db.session.query(User).all()
    return render_template('users.html', users=usersqs)


@app.route('/change_users', methods=['POST'])
@login_required
def change_users():
    if current_user.is_active and current_user.is_staff:
        data = request.json
        tablename = User.__tablename__
        current_ids = {i[0] for i in app.db.session.query(User.id).all()}
        saved_ids = {int(i['uid']) for i in data if i['uid']}
        ids_to_delete = list(current_ids.difference(saved_ids))
        app.db.session.query(User.id).filter(User.id.in_(ids_to_delete)).delete(synchronize_session='fetch')
        app.db.session.commit()
        errors = []
        for us in data:
            uid = us.get('uid', None)
            uname = us.get('username', None)
            password = us.get('password', None)
            active = us.get('active', False)
            staff = us.get('is_staff', False)
            if not uname:
                continue
            try:
                connection = app.db.session.connection()
                if uid:

                    if password:
                        _hash = user_manager.hash_password(password)
                        q = f"""UPDATE "{tablename}" SET "password" = '{_hash}';"""
                        connection.execute(q)
                    # TODO Обновлять только измененные строки
                    q = f"""UPDATE "{tablename}" SET "active" = '{active}', "is_staff" = '{staff}' 
                        WHERE "id" = '{uid}';"""
                    connection.execute(q)
                elif password:
                    _hash = user_manager.hash_password(password)
                    q = f"""INSERT INTO "{tablename}" ("username", "password", "active", "is_staff") 
                            VALUES ('{uname}', '{_hash}', '{active}', '{staff}');"""
                    connection.execute(q)
                else:
                    errors.append(f'Empty password for new user: {uname}!')
                app.db.session.commit()
            except exc.SQLAlchemyError as e:
                errors.append(str(e))
                print(str(e))
        # Delete users removed from table
        if not errors:
            status = 'Successful'
        else:
            status = f'Processed with {len(errors)} errrors'

    else:
        status = 'Permission denied'
    flash(status)
    return jsonify(status)


@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('static/js', path)
