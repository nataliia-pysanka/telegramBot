from flask import request, redirect, url_for, session, render_template
from flask import Flask
from flask_migrate import Migrate


app = Flask(__name__)

# db.init_app(app)
# migrate = Migrate(app, db)



@app.route('/', methods=['GET', 'POST'], strict_slashes=False)
def index():
    return render_template('pages/index.html')


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
@app.route('/signin', methods=['GET', 'POST'], strict_slashes=False)
def signin():
    executor.start_polling(dp)


