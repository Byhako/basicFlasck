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

# /cursos/fisica/logica
@app.route('/cursos/<curso1>/<curso2>')
def cursos(curso1, curso2):
    return '<h2>Selene estudia {} y {}</h2>'.format(curso1, curso2)

# /libros/2
@app.route('/libros/<int:id>/') # valido que sea numerico el parametro
def libros(id):
    return '<h2>Selene lee el libro {}</h2>'.format(id)

if __name__ == '__main__':
    app.run(debug=True, port=5001)