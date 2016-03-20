import unittest
from app.animal import Animal

class TestAnimal(unittest.TestCase):
 
    def setUp(self):
      self.tiger = Animal("Tiger")
      self.pheasant = Animal("Pheasant")
      self.lion = Animal("Lion")

    def test_animal_has_kind(self):
      self.assertEqual("Tiger", self.tiger.kind)

    def test_can_add_edible_animal(self):
      self.tiger.add_edible(self.pheasant.kind)
      self.assertEqual(1,len(self.tiger.edible_animals))
    
    def test_can_eat_animal(self):
      self.tiger.add_edible(self.pheasant.kind)
      self.assertEqual(True,self.tiger.eats(self.pheasant.kind))

    def test_cannot_eat_animal(self):
      self.tiger.add_edible(self.pheasant.kind)
      self.assertEqual(False,self.tiger.eats(self.lion.kind))


