from flask import Flask, render_template, request, make_response, session, redirect, url_for, flash
from flask_wtf import CsrfProtect
import json
import formulario

app = Flask(__name__)
app.secret_key = 'my_secret_key'
csrf = CsrfProtect(app)

@app.errorhandler(404)
def page_no_found(e):
    return render_template('404.html'), 404

@app.route('/')
def index():
    custom_cookie = request.cookies.get('custom_cookie', 'No encontrado.')
    print(custom_cookie)
    if 'username' in session:
        username = session['username']
        print(username)

    return render_template('index.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    comment_form = formulario.CommentForm(request.form)
    if request.method == 'POST' and comment_form.validate():
        username = comment_form.username.data
        session['username'] = username
        success_message = 'Bienvenido {}'.format(username)

        flash(success_message)
    else:
        print('Error')

    return render_template('login.html', form=comment_form)

@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username')
    # pasamos el nombre de la funcion que esta asociada a la ruta donde
    # queresmos redireccionar.
    return redirect(url_for('login'))

@app.route('/cookie')
def cookie():
    response = make_response( render_template('cookie.html') )
    response.set_cookie('custom_cookie', 'Selene')
    return response

@app.route('/ajax-login', methods = ['POST'])
def ajax_login():
    print(request.form)
    username = request.form['username']
    # validacion
    response = { 'status': 200, 'id': 1, 'username': username }
    return json.dumps(response)


if __name__ == "__main__":
    app.run(debug=True, port=8000)
