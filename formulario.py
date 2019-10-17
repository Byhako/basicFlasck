from wtforms import Form, StringField, TextField
from wtforms.fields.html5 import EmailField

class CommentForm(Form):
    username = StringField('usuario')
    email = EmailField('correo electrónico')
    comment = TextField('comentario')