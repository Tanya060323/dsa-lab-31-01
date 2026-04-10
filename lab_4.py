from flask import Flask, render_template_string, request, redirect, flash, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'secret-key'

# База данных
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Настройка Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login_get'


# Модель пользователя (таблица users)
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(200))
    name = db.Column(db.String(100))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# HTML-шаблоны
index_html = """
<h1>Лабораторная работа №4</h1>
<p>Разработка механизмов аутентификации и авторизации для WEB-приложений на Flask</p>
<p>В данной лабораторной работе реализована система аутентификации и авторизации на основе Flask<p>

<p>Добро пожаловать, {{ current_user.name }}!</p>

<a href="{{ url_for('logout') }}">Выход</a>
"""

login_html = """
<h2>Вход</h2>

<form method="POST">
    Email: <input type="email" name="email" required><br>
    Пароль: <input type="password" name="password" required><br>
    <button type="submit">Войти</button>
</form>

<p style="color:red;">
{% for message in get_flashed_messages() %}
    {{ message }}
{% endfor %}
</p>

<a href="{{ url_for('signup_get') }}">Регистрация</a>
"""

signup_html = """
<h2>Регистрация</h2>

<form method="POST">
    Имя: <input type="text" name="name" required><br>
    Email: <input type="email" name="email" required><br>
    Пароль: <input type="password" name="password" required><br>
    <button type="submit">Зарегистрироваться</button>
</form>

<p style="color:red;">
{% for message in get_flashed_messages() %}
    {{ message }}
{% endfor %}
</p>

<a href="{{ url_for('login_get') }}">Вход</a>
"""

# Главная страница
@app.route('/')
def index():
    if current_user.is_authenticated:
        return render_template_string(index_html)
    return redirect(url_for('login_get'))


# Отображение формы входа
@app.route('/login', methods=['GET'])
def login_get():
    return render_template_string(login_html)


@app.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()

    if not user:
        flash('Пользователь не найден')
        return redirect(url_for('login_get'))

    if not check_password_hash(user.password, password):
        flash('Неверный пароль')
        return redirect(url_for('login_get'))

    login_user(user)
    return redirect(url_for('index'))


# Отображение формы регистрации
@app.route('/signup', methods=['GET'])
def signup_get():
    return render_template_string(signup_html)


@app.route('/signup', methods=['POST'])
def signup_post():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()

    if user:
        flash('Пользователь уже существует')
        return redirect(url_for('signup_get'))

    hashed_password = generate_password_hash(password)

    new_user = User(email=email, password=hashed_password, name=name)

    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('login_get'))


# Выход из системы
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login_get'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)