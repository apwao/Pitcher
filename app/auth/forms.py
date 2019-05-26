from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,ValidationError,BooleanField
from wtforms.validators import Required,Email,EqualTo
from ..models import User

class RegistrationForm(FlaskForm):
    """
    class RegistrationForm to create a user from the information
    provided by a user during signing up.
    
    Args:
    FlaskForm: session secure base class provided by flask with csrf protection
    """
    email = StringField('Your Email Address', validators=[Required(),Email()])
    username = StringField('Enter your username', validators=[Required()])
    password = PasswordField('Password', validators=[Required(),EqualTo('password_confirm', message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords', validators=[Required()])
    submit = SubmitField('Sign Up')
    
    def validate_email(self,data_field):
        """
        validate_email method to compare user input email to the
        email saved in database when a user signs in
        """
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError("There is an account with email")
    def validate_username(self,data_field):
        """
        validate_username method to compare input username to username 
        saved in the database during logging in
        """
        if User.query.filter_by(username= data_field.data).first():
            raise ValidationError('That username is taken')
        
class LoginForm(FlaskForm):
    """
    class LoginForm to create a logged in user from the information
    provided by a user during logging in.
    
    Args:
    FlaskForm: session secure base class provided by flask with csrf protection
    """
    email = StringField('Your Email Address',validators=[Required(), Email()])
    password = PasswordField('Password',validators=[Required(),])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')
    