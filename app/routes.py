from flask import render_template, flash, redirect
from app import app
from app.forms import RegistationForm, LoginForm

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistationForm()
	if form.validate_on_submit():
	    return redirect(url_for('register'))
	return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		return redirect(url_for('login'))
	return render_template('login.html', title='Sign In', form=form)
