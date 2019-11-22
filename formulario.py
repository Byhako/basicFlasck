from wtforms import Form, StringField, TextField, validators, PasswordField
from wtforms.fields.html5 import EmailField

def length_honeypot(form, field):
    if len(field.data) > 0:
        raise validators.validationError('El campo debe estar vacio')

class LoginForm(Form):
    email = EmailField('Correo Electrónico',
        [
            validators.Email(message='Email invalido'),
            validators.Required(message='Password Requerido')
        ]
    )
    password = PasswordField('Contraseña',
        [
            validators.length(min=4, max=25, message='Longitud Incorrecta'),
            validators.Required(message='Password Requerido')
        ]
    )


class CreateForm(Form):
    username = TextField('Usuario',
        [
            validators.Required(message='Usuario Requerido')
        ]
    )
    email = EmailField('Correo Electrónico',
        [
            validators.Email(message='Email invalido'),
            validators.Required(message='Password Requerido')
        ]
    )
    password = PasswordField('Contraseña',
        [
            validators.length(min=4, max=25, message='Longitud Incorrecta'),
            validators.Required(message='Password Requerido')
        ]
    )