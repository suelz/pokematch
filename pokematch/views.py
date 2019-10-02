"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import request, render_template, session, redirect, url_for, jsonify
from flask_login import current_user, login_user, logout_user, LoginManager, login_required
from sqlalchemy import func, desc, asc, or_, and_
from . import app, db
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash
from .models import *
import hashlib
import os
import math
from math import sin, cos, sqrt, atan2, radians
import geopy.distance

PIC_PATH = "pics/"
ALLOWED_EXT = ["jpg", "jpeg", "png"]

def is_pic(filename):
    return '.' in filename and filename.split(".", 1)[1].lower() in ALLOWED_EXT

@app.route("/pics/<filename>")
def send_pic(filename):
    return send_from_directory(app.static_folder, filename)

def _min(one, two):
    if one < two:
        return one
    return two

M_TO_INT = {"Jan": 1,
            "Feb": 2,
            "Mar": 3,
            "Apr": 4,
            "May": 5,
            "Jun": 6,
            "Jul": 7,
            "Aug": 8,
            "Sep": 9,
            "Oct": 10,
            "Nov": 11,
            "Dec": 12
            }

@app.context_processor
def inject_year():
    return { "year": datetime.utcnow().year }

@app.route("/messages")
def messages():
    
    matches = Match.query.filter(Match.matcher_id==current_user.id)
    match_ids = []
    for match in matches:
        match_ids.append(match.matched_id)

    matches = Match.query.filter(Match.matched_id==current_user.id)
    for match in matches:
        match_ids.append(match.matcher_id)

    from sqlalchemy import and_

    messages = Message.query.filter(and_(Message.receiver.in_(match_ids), Message.sender==current_user.id))
    messages2 = Message.query.filter(and_(Message.sender.in_(match_ids), Message.receiver==current_user.id))

    messaged = {}
    for m in messages:
        if m.receiver not in messaged or m.timestamp > messaged[m.receiver][0].timestamp:
            try:
                match_ids.remove(m.receiver)
            except:
                pass
            messaged[m.receiver] = (m, User.query.filter(User.id==m.receiver).first())

    for m in messages2:
        if m.sender not in messaged or m.timestamp > messaged[m.sender][0].timestamp:
            try:
                match_ids.remove(m.sender)
            except:
                pass
            messaged[m.sender] = (m, User.query.filter(User.id==m.sender).first())

    unmessaged = User.query.filter(User.id.in_(match_ids)).all()
    return render_template("messages.html", unmessaged=unmessaged, messaged=messaged)

@app.route("/pictures")
def pictures():
    return render_template("pictures.html")

@app.route("/swipe/send_swipe/<int:u>/<direction>", methods=["POST"])
def send_swipe(u, direction):
    id = int(u)
    right = direction == "right"
    s = Swipe(matcher_id=current_user.id, matched_id=id, match=right)
    db.session.add(s)
    db.session.commit()

    if right:
        swiped = Swipe.query.filter(and_(Swipe.matcher_id == id,
                                        Swipe.matched_id == current_user.id))
        if swiped.count() != 0:
            m = Match(matcher_id = current_user.id, matched_id=id)
            db.session.add(m)
            db.session.commit()
            return jsonify(match=True)
    return jsonify(match=False)

@app.route("/swipe")
def swipe():
    swiped = Swipe.query.with_entities(Swipe.matched_id).filter(Swipe.matcher_id==current_user.id)
    potential = User.query.filter(and_(User.id != current_user.id, or_(current_user.preference == "both", current_user.preference == User.gender),User.id.notin_(swiped)))
    print("Potential=" + str(potential.count()) + " swiped=" + str(swiped.count()))
    soulmates = []
    for person in potential:
        dist = get_distance((person.lat, person.long),(current_user.lat, current_user.long))
        print("dist = " + str(dist) + person.name)
        if float(current_user.distance) < dist:
            print("Wrong distance " + person.name)
            del person
            continue
        age = get_age(person.birthday)
        if current_user.min > age or current_user.max < age:
            print("Wrong age " + person.name)
            del person
            continue
        print("Adding " + person.name)
        soulmate = (person, age, round(dist,1))
        soulmates.append(soulmate)
    print("num mates " + str(len(soulmates)))
    return render_template("swipe.html", soulmates=soulmates)

@app.route("/")
@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/portal")
def portal():
    return render_template("portal.html")

@app.route("/Edit")
def edit():
    return render_template("edit.html")

@app.route("/perform_login", methods=["POST"])
def perform_login():
    email = request.form["email"]
    password = request.form["password"]
    user = User.query.filter(func.lower(User.email) == func.lower(email)).first()
    if user is None or not user.check_password(password):
        return jsonify("Incorrect email or password")
    login_user(user)
    return jsonify(success=True, redirect=url_for("portal"))

@app.route("/logoff")
def logoff():
    logout_user()
    return redirect(url_for("login"))

@app.route('/perform_register', methods=["POST"])
def perform_register():
    u = User()
    try:
        u.email = request.form["name"]
        u.password = generate_password_hash(request.form["password"])
        u.name = request.form["name"]
        u.preference = request.form["preference"]
        u.gender = request.form["gender"]
        u.bio = request.form["bio"]
        u.birthday = datetime(int(request.form["year"]), M_TO_INT[request.form["month"]], int(request.form["day"]))
        u.min = _min(int(request.form["year"]) - 40, 18)
        u.max = int(request.form["year"]) + 20
        u.lat = float(request.form["lat"])
        u.long = float(request.form["long"])
        User.query.filter(func.lower(User.email) == func.lower(u.email)).first()
        if User.query.filter(func.lower(User.email) == func.lower(u.email)).first() is not None:
            return jsonify(success = False, reason="This email is already in use.")

        file = request.files["picture"] 
        if not is_pic(file.filename):
            return jsonify(success = False, reason="Invalid picture, it must be a png or a jpg.")
        filename = secure_filename(file.filename)
        shorthand = hashlib.md5((u.email + filename).encode("utf-8")).hexdigest() + ".png"
        fname = os.path.join(app.static_folder, shorthand)
        file.save(fname)
        u.picture = shorthand

        db.session.add(u)
        db.session.commit()
        login_user(User.query.filter(func.lower(User.email) == func.lower(u.email)).first())
        print("*" * 10 + " Successfully created user " + "*" * 10)
        return jsonify(success=True, redirect=url_for("portal"))
    except Exception as e:
        import traceback
        print(traceback.format_exc())

@app.route('/perform_edit', methods=["POST"])
def perform_edit():
    try:
        current_user.name = request.form["name"]
        current_user.preference = request.form["preference"]
        current_user.gender = request.form["gender"]
        current_user.bio = request.form["bio"]
        current_user.birthday = datetime(int(request.form["year"]), M_TO_INT[request.form["month"]], int(request.form["day"]))
        current_user.min = int(request.form["min"])
        current_user.max = int(request.form["max"])
        db.session.commit()
        return jsonify(success=True, redirect=url_for("portal"))
    except Exception as e:
        import traceback
        print(traceback.format_exc())

def get_age(bd): 
    return int((datetime.now() - bd).days / 365.2425)

def get_distance(origin, destination):
    return geopy.distance.vincenty(origin, destination).miles   


@app.route("/send_message", methods=["POST"])
def send_message():
    other = int(request.form["other_user"])
    msg = request.form["message"]
    matched = Match.query.filter(or_(and_(Match.matcher_id == current_user.id, Match.matched_id == other), and_(Match.matcher_id == other, Match.matched_id == current_user.id))).first()
    if matched is None:
        return jsonify(success=False, reason="Not matched.")
    m = Message(contents=msg, sender=current_user.id, receiver=other)
    db.session.add(m)
    db.session.commit()
    return jsonify(success=True)

@app.route("/dm/<int:other_userid>/")
def dm(other_userid):

    other = User.query.filter(User.id == other_userid).first()
    if other is None:
        return redirect(url_for("messages"))

    msgs = Message.query.filter(or_(and_(Message.sender == current_user.id, Message.receiver == other.id), \
                                 and_(Message.sender == other.id, Message.receiver == current_user.id))).order_by(asc(Message.timestamp)).all()

    return render_template("dm.html", other=other, msgs=msgs)
