from flask import render_template
from app import app
from app.forms import RegistrationForm

@app.route('/register')
def register():
	form = RegistrationForm()
	return render_template('register.html', title='Register', form=form)
