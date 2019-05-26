from flask import render_template, redirect, url_for, flash, request
from . import auth
from ..models import User 
from .forms import RegistrationForm, LoginForm
from .. import db
from flask_login import login_user, logout_user, login_required
# from ..email import mail_message

@auth.route('/login')
def login():
    """
    login function bound to the login route that verifies
    whether a user has an account with the application and 
    logs them in if they are already signed up
    """
    # Creating an instance of class LoginForm
    login_form = LoginForm()
    # If user has clicked submit and the form is validated
    if login_form.validate_on_submit():
        # Querying database for existence of the user through their email address
        user = User.query.filter_by(email =login_form.email.data).first()
        # Checking if the user account exists and the password is correct
        if user is not None and user.verify_password(login_form.password.data)
            # User is logged in
            login_user(user, login_form.remember.data)
            # After user logs in redirect them to the home page
            return redirect(request.args.get('next') or url_for('main.index'))
        # Flashing alert incase user exists but credentials dont match
        flash('Invalid password or username')
    title = "login"
    # Returning user to the login page incase the form was not validated
    return render_template('auth/login.html', login_form = login_form, title = title )

@auth.route('/register', methods = ['GET', 'POST'])
def register():
    """
    register function to create a new user in the database
    when a user signs up for the first time
    """
    
    form = RegistrationForm()
    if form.validate_on_submit():
        # Matching user input to the database models
        user = User(email = form.email.data, username =form.username.data, password=form.password.data)
        # Adding a new user
        db.session.add(user)
        # Saving the user and their credentials to the database
        db.session.commit()
        
        return reirect(url_for('auth.login'))
    title = "New Account"
    return render_template('/auth/register.html', registration_form =form)

        