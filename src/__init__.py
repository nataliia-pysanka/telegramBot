from flask import request, redirect, url_for, session, render_template
from flask import Flask
from flask_migrate import Migrate
from src.db import db
from src.repository import user_rep
from config import config


app = Flask(__name__)
app.config.from_object(config.Config)

db.init_app(app)
migrate = Migrate(app, db)


@app.before_reques
def before_func():
    auth = True if 'username' in session else False
    if not auth:
        token_user = request.cookies.get('user')
        if token_user:
            user = user_rep.get_user_by_token(token_user)
            if user:
                session['user'] = {'email': user.email, 'id': user.id}


@app.route('/', methods=['GET', 'POST'], strict_slashes=False)
def index():
    # return render_template('pages/index.html')
    auth = True if 'user' in session else False
    if request.method == 'POST':
        if request.form.get('signin_input'):
            return redirect("https://t.me/TEB_Team_test_bot")
        elif request.form.get('login_input'):
            return redirect(url_for('notes'))

    token_user = request.cookies.get('user')
    if token_user:
        user = user_rep.get_user_by_token(token_user)
    return render_template('pages/index.html', auth=auth, user=user)


# @app.route('/login', methods=['GET', 'POST'], strict_slashes=False)
# def login():
#     auth = True if 'user' in session else False
#     if request.method == "POST":
#         email = request.form.get('email')
#         password = request.form.get('password')
#         remember = request.form.get('remember')
#
#         user = users_repr.login(email, password)
#         if user is None:
#             return redirect(url_for('login'))
#
#         session['user'] = {'email': user.email, 'id': user.id}
#         response = make_response(redirect(url_for('index')))
#
#         if remember:
#             token = str(uuid.uuid4())
#             expire_date = datetime.now() + timedelta(days=10)
#             response.set_cookie('user', token, expires=expire_date)
#             users_repr.set_token(user, token)
#
#         return response
#     if auth:
#         return redirect(url_for('index'))
#     return render_template('pages/login.html')
#
#

