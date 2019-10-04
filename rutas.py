from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hola mundo</h1>'

# /saludo?nombre=Ruben
@app.route('/saludo')
def saludo():
    param = request.args.get('nombre', 'desconocido')
    return '<h2>Hola {}</h2>'.format(param)

if __name__ == '__main__':
    app.run(debug=True, port=3000)