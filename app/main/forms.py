from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, SelectField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    """
    class UpdateProfile to model user Input on their profile information
    to match class User in the database.
    """
    bio = TextAreaField("Tell us about yourself", validators=[Required()])
    submit = SubmitField('Submit')
    
class PitchForm(FlaskForm):
    postedBy = StringField('Posted by', validators=[Required()])
    