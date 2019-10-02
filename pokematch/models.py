from datetime import datetime
from flask_login import UserMixin
from . import db, login, app
from flask import url_for
from werkzeug.security import check_password_hash, generate_password_hash


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(db.Model, UserMixin):
    #__tablename__ = "User"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(32), index = True, nullable = False)
    email = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    bio = db.Column(db.String(256), nullable = False)
    birthday = db.Column(db.DateTime, nullable = False)
    distance = db.Column(db.Integer, default = 10000, nullable = False)
    gender = db.Column(db.String(12), nullable = False)
    preference = db.Column(db.String(12), nullable = False)
    min = db.Column(db.Integer, nullable = False)
    max = db.Column(db.Integer, nullable = False)
    lat = db.Column(db.Float, nullable = False)
    long = db.Column(db.Float, nullable = False)
    picture = db.Column(db.String(1024), nullable = False)

    def pic_path(self):
        return url_for("static", filename=self.picture)

    def set_password(self, unhashed : str):
        password = generate_password_hash(str)

    def check_password(self, unhashed : str):
        return check_password_hash(self.password, unhashed)


class Swipe(db.Model):
    #__tablename__ = "Swipe"

    id = db.Column(db.Integer, primary_key=True)
    matcher_id = db.Column(db.Integer, nullable = False)
    matched_id = db.Column(db.Integer, nullable = False)
    match_date = db.Column(db.DateTime, default=datetime.utcnow)
    match = db.Column(db.Boolean, nullable = False)

class Match(db.Model):
    #__tablename__ = "Match"

    id = db.Column(db.Integer, primary_key=True)
    matcher_id = db.Column(db.Integer, nullable = False)
    matched_id = db.Column(db.Integer, nullable = False)
    send_date = db.Column(db.DateTime, default=datetime.utcnow)

class Message(db.Model):
    #__tablename__ = "Message"

    id = db.Column(db.Integer, primary_key = True)
    contents = db.Column(db.String(1024), nullable = False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    sender = db.Column(db.Integer,db.ForeignKey('user.id'), nullable = False)
    receiver = db.Column(db.Integer,db.ForeignKey('user.id'), nullable = False)
    