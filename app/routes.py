from app import app
from flask import render_template

@app.route('/')
@app.route('/home')
def home():
    title = 'Home'
    return render_template('home.html', title=title)


# route for users registration

@app.route('/signup')
def signup():
    title = 'Sign Up'
    return render_template('signup.html', title=title)

