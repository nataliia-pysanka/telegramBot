from flask import request, redirect, url_for, session, render_template
from flask import Flask
from flask_migrate import Migrate
from src.db import db
from src.repository import user_rep
from config import config


app = Flask(__name__)
app.config.from_object(config.Config)

db.init_app(app)

with app.app_context():
    db.create_all()

migrate = Migrate(app, db)


@app.before_request
def before_func():
    """
    Method checks whether the user is authorized
    """
    auth = True if 'username' in session else False
    if not auth:
        token_user = request.cookies.get('user')
        if token_user:
            user = user_rep.get_user_by_token(token_user)
            if user:
                session['user'] = {'email': user.email, 'id': user.id}
            return user


@app.route('/', methods=['GET', 'POST'], strict_slashes=False)
def index():
    """
    Method loads main page
    """
    auth = True if 'user' in session else False
    if request.method == 'POST':
        if request.form.get('signin_input'):
            return redirect("https://t.me/TEB_Team_test_bot")
        elif request.form.get('login_input'):
            return redirect(url_for('login'))

    user = before_func()
    return render_template('pages/index.html', auth=auth, user=user)


@app.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def login():
    pass


@app.route('/sign', methods=['GET', 'POST'], strict_slashes=False)
def signin():
    pass





