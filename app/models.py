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