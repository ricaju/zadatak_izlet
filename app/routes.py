from flask import render_template, flash, redirect
from app import app
from app.forms import RegistationForm

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistationForm()
	if form.validate_on_submit():
	    return redirect('/register')
	return render_template('register.html', title='Register', form=form)
