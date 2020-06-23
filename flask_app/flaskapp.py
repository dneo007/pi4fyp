from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '9b0e29820c277b0c91faa0457f2b2cbb'

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
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for { form.username.data }!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title ='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == "admin" and form.password.data== "password":
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful', 'danger')
    return render_template('login.html', title ='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)
