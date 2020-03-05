from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, StringField


class LoginForm(FlaskForm):
    username = StringField('username')
    password = PasswordField('password')
