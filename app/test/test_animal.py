import unittest
from app.animal import Animal

class TestAnimal(unittest.TestCase):
 
    def setUp(self):
      self.animal = Animal("Tiger")

    def test_animal_has_name(self):
      self.assertEqual("Tiger", self.animal.name)