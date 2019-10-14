from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = 'Selene'
    return render_template('herencia1.html', name=name)

@app.route('/clientes')
def clientes():
    clients = ['Toto', 'Ana', 'Pepe', 'Matu']
    return render_template('herencia2.html', clients=clients)

if __name__ == '__main__':
    app.run(debug=True, port=8000)