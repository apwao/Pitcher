from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_login import UserMixin


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
    username = db.Column(db.String(50), index=True)
    password_hash = db.Column(db.String(255))
    users = db.relationship('User', backref='user_no', lazy='dynamic')
    email = db.Column(db.String(255), unique=True, index=True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    users_comments = db.relationship(
        'Comments', backref='comments', lazy='dynamic')

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
    


class Pitch(db.Model):
    """
    class Pitch to create instances of new pitches created by
    users once they are logged into the application.

    Args:
    db.Model: base class for user model 
    stored in the SQLAlchemy instance db
    """
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(10))
    pitchname = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pitch = db.relationship("Comments", backref="pitches", lazy="dynamic")


class Comments(db.Model):
    """
    class comment to create new comment objects to save in the database
    whenever a user comments on a pitch
    """
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String)
    comment_title = db.Column(db.String)
    posted = db.Column(db.DateTime, default=datetime.utcnow)
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('comments.id'))
