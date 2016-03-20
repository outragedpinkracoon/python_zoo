import unittest
from app.enclosure import Enclosure
from app.animal import Animal
 
class TestEnclosure(unittest.TestCase):
 
    def setUp(self):
      self.enclosure = Enclosure("Tigers",2)
      self.tiger = Animal("Tiger")
      self.pheasant = Animal("Pheasant")
      self.tiger.add_edible(self.pheasant.kind)
    
    def test_has_name(self):
      self.assertEqual("Tigers", self.enclosure.name)

    def test_has_capacity(self):
      self.assertEqual(2, self.enclosure.capacity)

    def test_can_add_animal(self):
      self.enclosure.add_animal(self.tiger)
      self.assertEqual(1, self.enclosure.number_of_animals())

    def test_cant_add_more_animals_than_capacity(self):
      self.enclosure.add_animal(self.tiger)
      self.enclosure.add_animal(self.tiger)
      self.enclosure.add_animal(self.tiger)
      self.assertEqual(2, self.enclosure.number_of_animals())

    def test_cant_add_animal_that_eats_enclosed_animal(self):
      self.enclosure.add_animal(self.tiger)
      self.enclosure.add_animal(self.pheasant)
      self.assertEqual(1, self.enclosure.number_of_animals())
      self.assertEqual(self.tiger.kind, self.enclosure.animals[0].kind)

    def test_returns_aggressive_animals(self):
      self.enclosure.add_animal(self.tiger)
      result = self.enclosure.aggressive_animals(self.pheasant.kind)
      self.assertEqual(1, len(result))
      self.assertEqual(self.tiger.kind, result[0].kind)