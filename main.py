from flask import Flask, render_template, request, make_response, session, redirect, url_for, flash, g
from flask_wtf.csrf import CSRFProtect
import json
import formulario
from config import DevelopmentConfig
from models import db, User, Comment

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
# app.secret_key = 'my_secret_key'
# csrf = CSRFProtect(app)
csrf = CSRFProtect()


@app.errorhandler(404)
def page_no_found(e):
    return render_template('app/404.html'), 404

# -----------------------------------------------------------------------
@app.before_request
def before_request():
    g.variable_global = 'Selene'
    print('\n --------------------------------------------- \n')
    if 'email' not in session and request.endpoint in ['comment', 'review']:
        return redirect(url_for('/'))
    
    elif 'email' in session and request.endpoint in ['login', 'create']:
        return redirect(url_for('index'))


@app.route('/')
def index():
    # print('index', g.variable_global)
    login = 'false'
    # Obtengo la cokie
    custom_cookie = request.cookies.get('custom_cookie', 'No encontrada')
    print('custom_cookie', custom_cookie)

    # Leo sesiones
    if 'email' in session:
        email = session['email']
        login = 'true'
        user = User.query.filter_by(email = email).first()
        session['user_id'] = user.id

    return render_template('app/index.html', login=login)


# @app.after_request
# def after_request(response):
#     # print('after', g.variable_global)
#     return response

# -----------------------------------------------------------------------


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = formulario.LoginForm(request.form)
    if request.method == 'POST' and login_form.validate():
        email = login_form.email.data
        password = login_form.password.data

        # select * fron users where mail='mail' limit 1
        user = User.query.filter_by(email = email).first()

        if user is not None and user.verify_password(password):
            success_message = 'Bienvenido {}'.format(login_form.email.data)
            flash(success_message)
            session['email'] = email
            return redirect(url_for('index'))
        else:
            error_message = 'correo o contraseña incorrecta'
            flash(error_message)

    return render_template('app/login.html', form=login_form)


@app.route('/logout')
def logout():
    if 'email' in session:
        session.pop('email')
        session.pop('user_id')
    # Ponemos el nombre de la funcion
    return redirect(url_for('login'))


@app.route('/cokie')
def cookie():
    response = make_response( render_template('app/cookie.html') )
    # Nombre de la cokie, valor
    response.set_cookie('custom_cookie', 'Selene')
    return response

@app.route('/comment', methods=['GET', 'POST'])
def comment():
    comment_form = formulario.CommentForm(request.form)
    if request.method == 'POST' and comment_form.validate():
        user_id = session['user_id']
        comment = Comment(
            user_id = user_id,
            text = comment_form.comment.data
            )
        
        db.session.add(comment)
        db.session.commit()

        success_message = 'Comentario creado con exito'
        flash(success_message)

    return render_template('app/comment.html', form=comment_form)

@app.route('/review')
@app.route('/review/<int:page>')
def review(page=1):
    per_page = 3
    ant = page - 1
    sig = page + 1
    if page == 1:
        ant = 1

    comments_list = Comment.query.join(User).add_columns(User.username, Comment.text).paginate(
        page, per_page, False)
        # en que pagina, numero de items por pagina
    if len(comments_list.items) < 3:
        sig = page
    return render_template('app/review.html', comments=comments_list, ant=ant, sig=sig)

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
            create_form.username.data,
            create_form.email.data,
            create_form.password.data
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
        print('db creada')
    app.run(port=5000)