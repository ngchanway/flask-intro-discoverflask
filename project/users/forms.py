from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired, Length, Email, EqualTo

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])

class RegistrationForm(FlaskForm):
    username = StringField(
        'username',
        validators=[InputRequired(), Length(min=3, max=25)]
    )
    email = EmailField(
        'email',
        validators=[InputRequired(), Email(), Length(min=6, max=40)]
    )
    password = PasswordField(
        'password',
        validators=[InputRequired(), Length(min=6, max=25)]
    )
    confirm = PasswordField(
        'Repeat password',
        validators=[InputRequired(), EqualTo('password', message='Password must match.')]
    )
