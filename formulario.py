from wtforms import Form, StringField, TextField, validators
from wtforms.fields.html5 import EmailField

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
    comment = TextField('comentario',
        [
            # validators.length(min=4, max=25, message='Usuario invalido'),
            validators.Required(message='Usuario es requerido')
        ]
    )