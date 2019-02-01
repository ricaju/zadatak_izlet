from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField, SelectField, TextAreaField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import DataRequired, EqualTo, Email
from app.models import User, Trip, Comments
from werkzeug.utils import secure_filename

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
    about = TextAreaField('About the trip', validators=[DataRequired()])
    picture = FileField('Picture', validators=[FileAllowed(['jpg', 'png'], 'Images only!')])
    submit = SubmitField('Submit')

class EditForm(FlaskForm):
    oldpassword = PasswordField('Old password')
    password = PasswordField('Password', )
    password2 = PasswordField('Password', [EqualTo('password')])
    first_name = StringField('First name')
    last_name = StringField('Last name')
    bio = StringField('bio')
    spol = SelectField('spol', choices=[('Male', 'Male'), ('Female', 'Female')])
    picture = FileField('Picture', validators=[FileAllowed(['jpg', 'png'], 'Images only!')])
    submit = SubmitField('Submit')

class TripPageForm(FlaskForm):
	comment = TextAreaField('Comment', validators=[DataRequired()])
	submit = SubmitField('Comment')

class JoinATripForm(FlaskForm):
    submit = SubmitField('Join A Trip')
    submit_cancel = SubmitField('Cancel A Trip')

class HomeSearchForm(FlaskForm):
    search = StringField('',validators=[DataRequired()])
    submit_destination = SubmitField('Search by destination')
    submit_rate = SubmitField('Search by rate')
    submit_price = SubmitField('Search by price')
    submit_date = SubmitField('Search by date')
    submit_username = SubmitField('Search by username')