from flask import render_template, flash, redirect, url_for, request
import os
from app import app, db
from app.forms import RegistrationForm, LoginForm, NewTripForm, NewPasswordForm, EditForm, TripPageForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Trip, Comments
from werkzeug.urls import url_parse
from werkzeug.utils import secure_filename

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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('home')
       	return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/home')
@login_required
def home():
    trip = Trip.query.first()
    if trip is not None:
        all_trips = Trip.query.all()
        data = []
        for trips in all_trips:
            trips_data = {'location' : trips.location, 'about' : trips.about, 'rating' : trips.trip_rating, 'cost' : trips.total_cost, 'id' : trips.id}
            data.append(trips_data)
        return render_template('home.html', title='Home', data= data)
    return render_template('home.html', title='Home')

@app.route('/home/my_trips')
@login_required
def my_trips():
    trip = Trip.query.first()
    if trip is not None:
        all_trips = Trip.query.filter_by(creator_id=current_user.id)
        data = []
        for trips in all_trips:
            trips_data = {'location' : trips.location, 'about' : trips.about, 'rating' : trips.trip_rating, 'cost' : str(trips.total_cost) + ' kn', 'id' : trips.id}
            data.append(trips_data)
        return render_template('home.html', title='Home', data= data)
    return render_template('home.html', title='Home')


@app.route('/trip/<id>', methods=['GET', 'POST'])
@login_required
def trip(id):
    trip = Trip.query.filter_by(id = id).first()
    user = User.query.filter_by(id = trip.creator_id).first()
    comments = Comments.query.filter_by(trip_id = trip.id)
    c_data = []
    if comments is not None:
    	for comment in comments:
    		user = User.query.filter_by(id = comment.user_id).first()
    		comment_data = {'comment' : comment.coments, 'username' : user.username}
    		c_data.append(comment_data)
    trip_data = {'trip' : trip.id, 'location' : trip.location, 'about' : trip.about, 'rating' : trip.trip_rating, 'cost' : str(trip.total_cost) + ' kn',
    'date' : trip.date.strftime('%d/%m/%Y'), 'transport' : trip.transport, 'creator' : user.username, 'comments' : c_data}
    form = TripPageForm()
    if form.validate_on_submit():
        comment = Comments(coments = form.comment.data, user_id = current_user.id, trip_id = trip.id)
        db.session.add(comment)
        db.session.commit()
        return render_template('trip.html', title='Trip', data = trip_data, form=form)
    return render_template('trip.html', title='Trip', data = trip_data, form=form)


@app.route('/newtrip', methods=['GET', 'POST'])
@login_required
def newtrip():
    form = NewTripForm()
    if form.validate_on_submit():
        #if form.picture:
           # import pdb; pdb.set_trace()
            #filename = secure_filename(form.picture.data.filename)
           # form.picture.data.save(os.path.join(app.config['UPLOAD_FOLDER']), filename)

        newtrip = Trip(location = form.location.data,
            transport= form.transport.data,
            min_people= int(form.min_people.data),
            max_people= int(form.max_people.data),
            about= form.about.data,
            date = form.date.data,
            total_cost = int(form.total_cost.data),
            creator_id = current_user.id)
        db.session.add(newtrip)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('newTrip.html', title='New Trip', form=form)

@app.route('/newpassword', methods=['GET', 'POST'])
def newpassword():
    form = NewPasswordForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None:
            flash('Invalid username')
            return redirect(url_for('newpassword'))
        user.set_password(form.password_new.data)
        db.session.add(user)
        db.session.commit()
        flash('You changed your password!')
        return redirect(url_for('login'))
    return render_template('newPassword.html', title='New Password', form = form)

@app.route('/edit', methods= ['GET', 'POST'])
@login_required
def edit():
    form = EditForm()
    if form.validate_on_submit():
        if not current_user.check_password(form.oldpassword.data):
            flash('Your old password isn\'t correct')
        else:
            current_user.set_password(form.password.data)

        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.bio = form.bio.data
        current_user.spol = form.spol.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', title='Edit Profile', form = form)

@app.route('/profile', methods = ['GET', 'POST'])
@login_required
def profile():

    return render_template('profile.html', title="Profile")
