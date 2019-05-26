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
    """
    class pitchform that renders form fields and processes the data entered by
    a user to enable them to create and submit their pitches
    """
    postedBy = StringField('Posted by', validators=[Required()])
    pitch = TextAreaField('Pitch')
    category = SelectField('Choose a category for your pitch', choices=[('Interview', 'Interview_pitch'),('Product','Product_pitch'),('Pickup','Pickup_lines'),('promotion','promotion_pitch')])
    submit = SubmitField('Submit')
    
class CommentForm(FlaskForm):
    """
    class CommentForm that renders form fields to enable a user to comment 
    on the pitches submitted by others
    """
    postedBy = StringField('PostedBy', validators=[Required()])
    title = StringField('Comment')
    comment = TextAreaField('Please enter a comment')
    sumit = SubmitField('submit')
    
    