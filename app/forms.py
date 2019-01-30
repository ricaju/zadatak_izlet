from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField
from wtforms.validators import DataRequired, EqualTo, Email
from app.models import User, Trip

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Password', validators=[DataRequired(), EqualTo('password')])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Register')


    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')


class LoginForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	submit = SubmitField('Login')
	remember_me = BooleanField('Remember Me')

class NewPasswordForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    password_new = PasswordField('Password', validators=[DataRequired()])
    password_check = PasswordField('Password', validators = [DataRequired(), EqualTo('password_new')])
    submit = SubmitField('Login')

class NewTripForm(FlaskForm):
    location = StringField('Location', validators=[DataRequired()])
    date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
    transport = StringField('Transportation', validators=[DataRequired()])
    min_people = StringField('Minimum people', validators=[DataRequired()])
    max_people = StringField('Maximum people', validators=[DataRequired()])
    total_cost = StringField('Total_cost', validators=[DataRequired()])
    about = StringField('About the trip', validators=[DataRequired()])
    submit = SubmitField('New Trip')

class EditForm(FlaskForm):
    username = StringField('username')
    email = StringField ('Email', validators=[Email()])
    firstName = StringField('First name')
    lastName = StringField('Last name')
    bio = StringField('bio')
