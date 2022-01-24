from crypt import methods
from app import app
from flask import render_template, flash, redirect
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

@app.route('/login', methods=['GET', 'POST'] )
def login():
    title = 'Login Form'
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'
            .format(form.username.data, form.remember_me.data))
        return redirect('/home')
    return render_template('login.html', title=title, form=form)


