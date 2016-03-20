import unittest
import exceptions
from app.zoo import Zoo
from app.enclosure import Enclosure
 
class TestZoo(unittest.TestCase):
 
    def setUp(self):
      self.zoo = Zoo(10, "My Zoo")
      self.tigers = Enclosure("Tigers",2)

    def test_has_capacity(self):
      self.assertEqual(10, self.zoo.capacity)

    def test_has_name(self):
      self.assertEqual("My Zoo", self.zoo.name)
  
    def test_can_set_name(self):
      self.zoo.name = "Super Zoo"
      self.assertEqual("Super Zoo", self.zoo.name)

    def test_cannot_set_capacity(self):
      with self.assertRaises(AttributeError):
        self.zoo.capacity = 1000

    def test_can_add_enclosures(self):
      self.zoo.add_enclosure(self.tigers)
      self.assertEqual(1, self.zoo.number_of_enclosures())




