from flask import render_template, url_for, flash, redirect, request, jsonify
from flaskapp import app, db, bcrypt
from flaskapp.forms import RegistrationForm, LoginForm
from flaskapp.models import User, Post, Reading
from flask_login import login_user, current_user, logout_user, login_required
import json
from flaskapp.dbquery import dbquery, dbquery2

posts = [
    {
        'author': 'Darren Neo',
        'title' : 'Results',
        'content': 'First Post Content',
        'date_posted': 'June 21, 2020'
    },
    {
        'author': 'Darren Neo',
        'title' : '2nd Result',
        'content': '2nd Post Content',
        'date_posted': 'June 22, 2020'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title ='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title ='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/chart', methods=['GET', 'POST'])
def chart():
    # readings = Reading.query.all()
    id = []
    sensor = dbquery()
    print(sensor)
    # for reading in readings:
    #     # id.append(reading.id)
    #     sensor.append(reading.id)
    data = {
        # "id": id,
        "sensor": sensor
    }
    return render_template('chart.html', title='Chart', data=data)

@app.route('/json', methods=['GET', 'POST'])
def json():
    sensor = dbquery()
    id = dbquery2()
    print(sensor)
    # for reading in readings:
    #     # id.append(reading.id)
    #     sensor.append(reading.id)
    data = {
        "id": id,
        "sensor": sensor
    }
    return jsonify(data)

@app.route('/account')
@login_required
def account():
    return render_template('account.html', title ='Account')
