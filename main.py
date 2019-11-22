from flask import Flask, render_template, request, make_response, session, redirect, url_for, flash, g
from flask_wtf.csrf import CSRFProtect
import json
import formulario
from config import DevelopmentConfig
from models import db, User

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
# app.secret_key = 'my_secret_key'
# csrf = CSRFProtect(app)
csrf = CSRFProtect()


@app.errorhandler(404)
def page_no_found(e):
    return render_template('app/404.html'), 404

# -----------------------------------------------------------------------
# @app.before_request
# def before_request():
#     g.variable_global = 'Selene'
#     # if 'username' not in session and request.endpoint not in ['index']:
#     #     return redirect(url_for('index'))


@app.route('/')
def index():
    # print('index', g.variable_global)

    # Obtengo la cokie
    custom_cookie = request.cookies.get('custom_cookie', 'No encontrada')
    print('custom_cookie', custom_cookie)

    # Leo sesiones
    if 'username' in session:
        username = session['username']
        print('username', username)
    return render_template('app/index.html')


# @app.after_request
# def after_request(response):
#     # print('after', g.variable_global)
#     return response

# -----------------------------------------------------------------------


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = formulario.LoginForm(request.form)
    if request.method == 'POST' and login_form.validate():
        print('email: ', login_form.email.data)
        print('password: ', login_form.password.data)
        session['username'] = login_form.email.data

        success_message = 'Bienvenido {}'.format(login_form.email.data)
        print(success_message)
        flash(success_message)

    return render_template('app/login.html', form=login_form)


@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username')
    # Ponemos el nombre de la funcion
    return redirect(url_for('login'))


@app.route('/cokie')
def cookie():
    response = make_response( render_template('app/cookie.html') )
    # Nombre de la cokie, valor
    response.set_cookie('custom_cookie', 'Selene')
    return response


@app.route('/ajax_login', methods = ['POST'])
def ajax_login():
    print('PETICION: ', request.form)
    email = request.form['email']
    # Validacion

    response = { 'status': 200, 'id': 1, 'email': email }
    return json.dumps(response)


@app.route('/create', methods=['GET', 'POST'])
def create():
    create_form = formulario.CreateForm(request.form)
    if request.method == 'POST' and create_form.validate():
        print('username: ', create_form.username.data)
        print('email: ', create_form.email.data)
        print('password: ', create_form.password.data)

        user = User(
            username = create_form.username.data,
            email = create_form.email.data,
            password = create_form.password.data
        )

        db.session.add(user)
        db.session.commit()

        success_message = 'Usuario {} creado con exito'.format(create_form.username.data)
        flash(success_message)

    return render_template('app/create.html', form=create_form)


if __name__ == "__main__":
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(port=5000)