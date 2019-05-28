import unittest
from app.models import Pitch

class TestPitch(unittest.TestCase):
    def setUp(self):
        self.new_pitch = Pitch( id='4',title='Cheesy', category = 'pickupline', pitchname="Are you from France coz I Eiffel you", posted="2019-05-27 14:15:43.587649",posted_by="Ivy")

    def tearDown(self):
        Pitch.query.delete()
        
    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.id, '4')
        self.assertEquals(self.new_pitch.title, 'Cheesy')
        self.assertEquals(self.new_pitch.category, 'pickupline')
        self.assertEquals(self.new_pitch.pitchname, 'Are you from France coz I Eiffel you')
        self.assertEquals(self.new_pitch.posted, '2019-05-27 14:15:43.587649')
        self.assertEquals(self.new_pitch.posted_by, 'Ivy')
    

if __name__ == "__main__":
    unittest.main()