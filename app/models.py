from . import db

class User (db.Model):
    """
    class User to create instances of new users signing up
    with the application.
    
    Args:
    db.Model: base class for user model 
    stored in the SQLAlchemy instance db
    """
    __tablename__ = 'users'
     
    id = db.Column(db.Integer,primary_key =True)
    username = db.Column(db.String(50), index = True)
    password_hash = db.Column(db.String(255))
    users = db.relationship('User', backref = 'user_no', lazy = 'dynamic')
    
class Pitch(db.Model):
    """
    class Pitch to create instances of new pitches created by
    users once they are logged into the application.
    
    Args:
    db.Model: base class for user model 
    stored in the SQLAlchemy instance db
    """   
    id = db.Column(db.Integer, primary_key = True)
    category = db.Column(db.String(10))
    pitchname = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pitch=db.relationship("Comments",backref="pitches", lazy="dynamic")
    
class Comments(db.Model):
    """
    class comment to create new comment objects to save in the database
    whenever a user comments on a pitch
    """
    __tablename__ = 'comments'
    
    id = db.Column(db.Integer, primary_key = True)
    comment = db.Column(db.String)
    comment_title = db.Column(db.String)
    posted = db.Column(db.DateTime, default=datetime.utcnow)
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('comments.id'))