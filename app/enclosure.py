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
      if(self.number_of_animals() < self._capacity):
        self._animals.append(animal)

    def number_of_animals(self):
      return len(self._animals)
    

    