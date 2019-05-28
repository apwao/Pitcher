import unittest
from app.models import User
from app import db

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user_Ayana = User(username='Ayana', password="booboo", email="ayana@yahoo.com", id=5, bio="I am a life enthusiast and a free spirit", profile_pic_path="app/static/photos")

    def tearDown(self):
        User.query.delete()
        
    def test_check_instance_variables(self):
        self.assertEquals(self.user_Ayana.id, 5)
        self.assertEquals(self.user_Ayana.username,'Ayana')
        self.assertEquals(self.user_Ayana.bio, 'I am a life enthusiast and a free spirit')
        self.assertEquals(self.user_Ayana.postedAt, '2019-05-23 14:15:43.587649')
        self.assertEquals(self.user_Ayana.email, 'ayana@yahoo.com')
        self.assertEquals(self.user_Ayana.profile_pic_path, 'app/static/photos')



    def test_password_setter(self):
        self.assertTrue(self.user_Ayana.password_hash is not None)

    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.user_Ayana.password

    def test_password_verification(self):
        self.assertTrue(self.user_Ayana.verify_password('booboo'))

if __name__ == "__main__":
    unittest.main()