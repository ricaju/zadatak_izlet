from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/register')
def register():
	form = LoginForm()
	return render_template('register.html', title='Register', form=form)
