from flask import Flask, render_template, request, make_response, session, redirect, url_for
from flask_wtf import CsrfProtect
import formulario

app = Flask(__name__)
app.secret_key = 'my_secret_key'
csrf = CsrfProtect(app)

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
        # print('username: ', comment_form.username.data)
        session['username'] = comment_form.username.data
    else:
        print('Error')

    return render_template('form.html', form=comment_form)

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

@app.route('/comment', methods = ['GET', 'POST'])
def comment():
    pass

if __name__ == "__main__":
    app.run(debug=True, port=8000)
