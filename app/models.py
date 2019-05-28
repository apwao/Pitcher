from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User (UserMixin, db.Model):
    """
    class User to create instances of new users signing up
    with the application.

    Args:
    db.Model: base class for user model 
    stored in the SQLAlchemy instance db
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), index=True)
    password_hash = db.Column(db.String())
    users = db.relationship('Pitch', backref='user_no', lazy='dynamic')
    email = db.Column(db.String(), unique=True, index=True)
    bio = db.Column(db.String())
    profile_pic_path = db.Column(db.String())
    users_comments = db.relationship('Comments', backref='user_comment', lazy='dynamic')

    # making password to be read only
    @property
    def password(self):
        """
        password function to make password read-only so that it cannot 
        be edited by an unauthorized user
        """
        raise AttributeError('You cannot read password attribute')
    @password.setter
    def password(self,password):
        """
        password function to generate a password hash and
        enable the read only password attribute to be editable
        """
        self.password_hash=generate_password_hash(password)
    def verify_password(self,password):
        """
        verify_password function to compare the password entered 
        to the password in the database during logging in
        """
        # inbuilt function to compare passwords
        return check_password_hash(self.password_hash,password)
    
    def __repr__(self):
        return f'User{self.username}'
    
class Pitch(db.Model):
    """
    class Pitch to create instances of new pitches created by
    users once they are logged into the application.

    Args:
    db.Model: base class for user model 
    stored in the SQLAlchemy instance db
    """
    __tablename__= "pitches"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    category = db.Column(db.String())
    pitchname = db.Column(db.String)
    posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pitch = db.relationship("Comments", backref="pitches", lazy="dynamic")
    posted_by =db.Column(db.String)

    def save_pitch(self):
        """
        save pitch method to save new pitches created by 
        users to the database
        """
        db.session.add(self)
        db.session.commit()

class Comments(db.Model):
    """
    class comment to create new comment objects to save in the database
    whenever a user comments on a pitch
    """
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String())
    comment_title = db.Column(db.String())
    posted = db.Column(db.DateTime, default=datetime.utcnow)
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    posted_by= db.Column(db.String)

    def save_comment(self):
        """
        save_comment method to save a new comment to the database
        """
        db.session.add(self)
        db.session.commit()