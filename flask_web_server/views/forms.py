from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, DateField, SubmitField
from wtforms.validators import Email, Length, Optional, DataRequired


class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(min=4, max=12)])
    password = PasswordField('password', validators=[DataRequired(), Length(min=8, max=80)])
    submit = SubmitField('submit')

class RegisterForm(FlaskForm):
    firstname = StringField('firstname', validators=[Length(min=4, max=12)])
    lastname = StringField('lastname', validators=[Length(min=4, max=12)])
    username = StringField('username', validators=[DataRequired(), Length(min=4, max=12)])
    email = StringField('email', validators=[DataRequired(), Email(message='Invalid email'), Length(max=50)])
    password = PasswordField('password', validators=[DataRequired(), Length(min=8, max=80)])
    confirm_password = PasswordField('confirm_password', validators=[DataRequired(), Length(min=8, max=80)])
    country = StringField('country', validators=[DataRequired(), Length(min=3, max=15)])
    language = StringField('language', validators=[DataRequired(), Length(min=3, max=15)])
    birthdate = DateField('birthdate', format='%m/%d/%Y', validators=[Optional()])
    submit = SubmitField('submit')    