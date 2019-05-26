from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, SelectField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    """
    class UpdateProfile to model user Input on their profile information
    to match class User in the database.
    """
    # Creating instances of form fields
    bio = TextAreaField("Tell us about yourself", validators=[Required()])
    submit = SubmitField('Submit')
    
class PitchForm(FlaskForm):
    postedBy = StringField('Posted by', validators=[Required()])
    pitch = TextAreaField('Pitch')
    category = SelectField('Choose a category for your pitch', choices=[('Interview', 'Interview_pitch'),('Product','Product_pitch'),('Pickup','Pickup_lines'),('promotion','promotion_pitch')])
    submit = SubmitField('Submit')