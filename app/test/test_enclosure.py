import unittest
from app.enclosure import Enclosure
from app.animal import Animal
 
class TestEnclosure(unittest.TestCase):
 
    def setUp(self):
      self.enclosure = Enclosure("Tigers",2)

    def test_has_name(self):
      self.assertEqual("Tigers", self.enclosure.name)

    def test_has_capacity(self):
      self.assertEqual(2, self.enclosure.capacity)

    def test_can_add_animal(self):
      self.enclosure.add_animal(Animal("Tiger"))
      self.assertEqual(1, self.enclosure.number_of_animals())