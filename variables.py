from flask import Flask, render_template

app = Flask(__name__)

@app.route('/user/<name>')
def user(name = 'Selene'):
    numbers = [1, 2, 3, 4]
    return render_template('user.html', name=name, numbers=numbers, edad=21)

if __name__ == '__main__':
    app.run(debug=True, port=3000)