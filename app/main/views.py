from flask import render_template,request,redirect, url_for,abort
from . import main
from flask_login import login_required, current_user
from ..models import User, Pitch, Comments
from .. import db, photos
from .forms import UpdateProfile, PitchForm, CommentForm
import markdown2

# home page
@main.route('/')
def index():
    """
    index function to render the home page anytime a user 
    logs into the application
    """
    pitches = Pitch.query.all()
    title = 'Pitch'
    return render_template('index.html', title = title, pitches = pitches)

# creating a new pitch
# user must be logged in to create a pitch
@main.route('/new/pitch', methods = ['GET', 'POST'])
@login_required
def new_pitch():
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
        title = form.title.data
        category =form.category.data
        
        # matching user input to model for pitches in database
        new_pitch = Pitch(pitchname = pitch, category =category, title = title, posted_by=current_user.username)
        new_pitch.save_pitch() 
        # return user to home after logging in  
        return redirect(url_for('.index'))
    return render_template("new_pitch.html", form=form)
 
# Add new comment   
@main.route('/comment/<int:id>', methods = ['GET', 'POST'])
@login_required
def comment(id):
    """
    function new_comment that enables a user to comment on a pitch and submit
    their comment 
    """
    pitch = Pitch.query.filter_by(id=id).first()
    comments=Comments.query.filter_by(pitch_id=pitch.id).all()
    form = CommentForm()
    
    if form.validate_on_submit():
        title = form.title.data
        comment = form.comment.data
        
        new_comment = Comments(comment_title = title, comment = comment, user_comment=current_user, pitch_id=id, posted_by=current_user.username)
        new_comment.save_comment()
        return redirect(url_for('.comment',id=pitch.id))
    return render_template('comment.html',form=form, pitch=pitch, comments=comments)
    
# Access user profile
@main.route('/user/<uname>')
@login_required
def profile(uname):
    """
    profile function to enable user access their own profile
    """
    # Querying database for user information
    user = User.query.filter_by(username=uname)
    # Accessing the pitches available in the database
    index = Pitch.query.filter_by(user_id=current_user.id).all()
    # checking if the user exists in the database
    if user is None:
        abort(404)
       
    return render_template('profile/profile.html', user = user, index = index)

# Allow user to make changes to their own profile
@main.route('/user/<uname>/update', methods = ['GET','POST'])
@login_required
def update_profile(uname):
    """
    update_profile function to enable a user to create
    their bio and add it to their profile
    """
    # # Check if user has an account
    # user = User.query.filter_by(username=uname)
    # if user is None:
    #     abort(404)
        
    # update_form = UpdateProfile()
    
    # if update_form.validate_on_submit():
    #     user.bio = update_form.bio.data
        
    #     db.session.add(user)
    #     db.session.commit()
        
    #     return redirect(url_for('.profile', uname = user.username))
    # return render_template('profile/update.html', update_form=update_form)
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)
        
    form = UpdateProfile()
    if form.validate_on_submit():
        user.bio = form.bio.data
        
        db.session.add(user)
        db.session.commit()
        
        return redirect(url_for('.profile', uname=user.username))
    return render_template('profile/update.html', form=form)
    
    

@main.route('/user/<uname>/update/pic', methods =['POST'])
@login_required
def update_pic(uname):
    """
    update pic function to facilitate uploading a profile photo and
    saving it to the database as well as displaying the profile picture 
    on the page
    """
    user = User.query.filter_by(username=uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        
        path = f'photos/{filename}'
        user.profile_pic_path = path
        
        db.session.commit()
    return redirect(url_for('main.profile', uname=uname))

@main.route('/pitch/<int:id>')
def view_pitch(id):
    """
    view_pitch function to help user view a specific pitch by clicking on it
    """
    pitch = Pitch.query.get(id)

    return render_template('pitch.html', pitch = pitch)

@main.route('/comment/<int:id>')
def view_comment(id):
    """
    view_comment function to help user view a specific comment upon 
    clicking on it
    """
    comment = Comments.query.get(id)
    
    return render_template('comment.html',comment = comment)
    