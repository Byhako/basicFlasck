from flask import Flask, render_template
import formulario

app = Flask(__name__)
@app.route('/')
def index():
  comment_form = formulario.CommentForm()
  return render_template('form.html', form=comment_form )

if __name__ == "__main__":
    app.run(debug=True, port=5000)