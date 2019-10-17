from flask import Flask, render_template, request
import formulario

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    comment_form = formulario.CommentForm(request.form)
    print('hola')
    if request.method == 'POST' and comment_form.validate():
        print('username: ', comment_form.username.data)
        print('email: ', comment_form.email.data)
        print('comment: ', comment_form.comment.data)

    return render_template('form.html', form=comment_form)

if __name__ == "__main__":
    app.run(debug=True, port=5000)