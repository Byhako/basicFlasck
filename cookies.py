from flask import Flask, render_template, request, make_response
from flask_wtf import CsrfProtect
import formulario

app = Flask(__name__)
app.secret_key = 'my_secret_key'
csrf = CsrfProtect(app)

@app.route('/')
def index():
    custom_cookie = request.cookies.get('custom_cookie', 'No encontrado.')
    print(custom_cookie)
    return render_template('index.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    comment_form = formulario.CommentForm(request.form)
    if request.method == 'POST' and comment_form.validate():
        print('username: ', comment_form.username.data)
        print('email: ', comment_form.email.data)
        print('comment: ', comment_form.comment.data)
    else:
        print('Error')

    return render_template('form.html', form=comment_form)


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
