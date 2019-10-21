from wtforms import Form, StringField, TextField, validators, HiddenField
from wtforms.fields.html5 import EmailField


def length_honeypot(form, field):
    if len(field.data) > 0:
        raise validators.ValidationError('El campo debe estar vacio')

class CommentForm(Form):
    username = StringField('usuario',
        [
            validators.length(min=4, max=25, message='Usuario invalido'),
            validators.Required(message='Usuario es requerido')
        ]
    )
    email = EmailField('correo electrónico',
        [
            validators.Email(message='Email invalido'),
        ]
    )
    comment = TextField('comentario')
    honeypot = HiddenField('', [length_honeypot])