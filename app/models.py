from datetime import datetime
from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64),index=True,unique=True)
    email = db.Column(db.String(120),index=True,unique=True)
    password_hash = db.Column(db.String(128))

    

class Trip(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    location = db.Column(db.String(120),index=True)
    about = db.Column(db.String(1000),index=True)
    date = db.Column(db.DateTime,index=True)
    min_people = db.Column(db.String(120),index=True)
    max_people = db.Column(db.String(120),index=True)
    cost = db.Column(db.Integer,index=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    creator_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    trip_rating = db.Column(db.Integer)

class User_rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_rating = db.Column(db.Integer)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))

