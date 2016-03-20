class Enclosure(object):

    def __init__(self, name, capacity):
      self._name = name
      self._animals = []
      self._capacity = capacity

    @property
    def name(self):
      return self._name

    @property
    def capacity(self):
      return self._capacity

    def add_animal(self, animal):
      if(self.number_of_animals() >= self._capacity):
        return

      if(self.contains_aggressive_animal(animal.kind)):
        return

      self._animals.append(animal)

    def aggressive_animals(self,kind):
      result = []
      for animal in self._animals:
        eats = animal.eats(kind)
        if(eats):
          result.append(animal)
      return result

    def contains_aggressive_animal(self, kind):
      return len(self.aggressive_animals(kind)) > 0
      
    def number_of_animals(self):
      return len(self._animals)

    @property
    def animals(self):
        return self._animals
    
    

    