from wtforms import Form, StringField
from wtforms import EmailField
from wtforms import validators
from wtforms.validators import InputRequired, Regexp, EqualTo

import re

def passwords_validation(form,field):
    print("La contraseña ingresada es: ",field.data)
    if not (re.findall("^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[.,@#$%^&+=]).*$", field.data)):
        raise validators.ValidationError('Ingrese una contraseña valida!')


class LoginForm(Form):
    username = StringField('usuario')
    password = StringField('contraseña')
    # password = StringField('contraseña')
    
class RegisterForm(Form):
    name = StringField('nombre',[InputRequired()])
    apellido = StringField('nombre',[InputRequired()])
    email = EmailField('email',[InputRequired()])
    username = StringField('usuario',[InputRequired()])
    password1 = StringField('contraseña',[InputRequired(), Regexp(regex="^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[.,@#$%^&+=]).*$",message="Ingrese una contraseña valida!"), EqualTo('password2',message='Las contraseñas no coinciden!')])
    password2 = StringField('repetir contraseña',[InputRequired(), Regexp(regex="^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[.,@#$%^&+=]).*$",message="Ingrese una contraseña valida!")])