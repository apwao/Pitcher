import unittest
from app.models import User, Comments
from flask_login import current_user
from app import db

class TestComments(unittest.TestCase):
    def setUp(self):        
        self.new_comment = Comments(pitch_id=2, comment="Works anytime", comment_title="Great!", postedAt="2019-05-27 14:15:43.587649", posted_by="Ivy")

    def tearDown(self):
        Comments.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.pitch_id, 2)
        self.assertEquals(self.new_comment.title, 'Great')
        self.assertEquals(self.new_comment.comment, 'Works anytime')
        self.assertEquals(self.new_comment.postedAt, '2019-05-27 14:15:43.587649')
        self.assertEquals(self.new_comment.posted_by, 'Ivy')