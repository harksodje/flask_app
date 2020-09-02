from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
class RegistrationForm(Form):
    username = StringField('username', validators = [DataRequired(), Length(min = 2, max = 20)])
    email = StringField('email', validators =[DataRequired(), Email()])
    password = PasswordField(' Password', validators = [DataRequired()])
    #EqualTo is used to confirm the password if the password enter is the same.
    confirm_password =PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password')])
    submit  = SubmitField('Sign up')

class LoginForm(Form):
    email = StringField('Email', validators =[DataRequired(), Email()])
    password = PasswordField('Confirm Password', validators = [DataRequired( )])
    remember = BooleanField ('Remeber Me')
    submit  = SubmitField('Sign up')