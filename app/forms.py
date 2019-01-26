from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email
from app.models import User

class RegistationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Password', validators=[DataRequired(), EqualTo('password')])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Register')


    def validation_user(self, username):
    	user = User.query.filter_by(username=username.data).first()
    	if user is not None:
    		raise ValidationError('Please use a different username.')

    def validation_email(self, email):
    	user = User.query.filter_by(email=email.data).first()
    	if user is not None:
    		raise ValidationError('Please use a different email')


class LoginForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	submit = SubmitField('Login')
	remember_me = BooleanField('Remember Me')

