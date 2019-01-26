from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import RegistationForm, LoginForm, NewTripForm

@app.route('/register', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		return redirect(url_for('login'))
	return render_template('login.html', title='Sign In', form=form)

@app.route('/home')
def home():
	return render_template('home.html', title='Home')

@app.route('/trip')
def trip():
	return render_template('trip.html', title='Trip')

@app.route('/newtrip', methods=['GET', 'POST'])
def newtrip():
	form = NewTripForm()
	if form.validate_on_submit():
		return redirect(url_for('newTrip.html'))
	return render_template('newTrip.html', title='New Trip', form=form)

