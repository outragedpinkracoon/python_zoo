import unittest
from app.enclosure import Enclosure
 
class TestEnclosure(unittest.TestCase):
 
    def setUp(self):
        self.enclosure = Enclosure("Tigers")

    def test_enclosure_has_name(self):
        self.assertEqual("Tigers", self.enclosure.name)