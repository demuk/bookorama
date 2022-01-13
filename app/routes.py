from app import app
from flask import render_template
from app.forms import LoginForm

@app.route('/')
@app.route('/home')
def home():
    title = 'Home'
    return render_template('home.html', title=title)


# route for users registration

@app.route('/signup')
def signup():
    title = 'Sign Up Form'
    return render_template('signup.html', title=title)



# route for users login

@app.route('/login')
def login():
    title = 'Login Form'
    form = LoginForm()
    return render_template('login.html', title=title, form=form)


