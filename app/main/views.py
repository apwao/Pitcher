from flask import render_template,request,redirect, url_for,abort
from . import main
from flask_login import login_required, current_user
from ..models import User, Pitch, Comments
from .. import db, photos
from .forms import UpdateProfile, PitchForm, CommentForm

# home page
@main.route('/')
def index():
    """
    index function to render the home page anytime a user 
    logs into the application
    """
    title = 'Pitch'
    return render_template('index.html', title = title)

# creating a new pitch
@main.route('/new/pitch/<int:id>', methods = ['GET', 'POST'])
# user must be logged in to create a pitch
@login_required
def new_pitch(id):
    """
    function new_pitch to enable a user to input and submit their
    new pitch and have it saved in the database
    
    Args:
    id: User id to keep track of which user made the pitch
    """
    # create an instance of class PitchForm
    form = PitchForm()
    if form.validate_on_submit():
        pitch = form.pitch.data
        
        # matching user input to model for pitches in database
        new_pitch = Pitch(pitchname = pitch, category =form.category.data, user = current_user  )
        new_pitch.save_pitch() 
        # return user to home after logging in  
        return redirect(url_for('.index'))
    
@main.route('/new/comment/<int: id>', methods = ['GET', 'POST'])
@login_required
def new_comment(id):
    """
    function new_comment that enables a user to comment on a pitch and submit
    their comment 
    """
    form = CommentForm()
    if form.validate_on_submit():
        title = form.title.data
        comment = form.comment.data
        
        new_comment = Comments(comment_title = title, comment = comment, useer = current_user)
        new_comment.save_comment()
        return redirect(url_for('.index'))