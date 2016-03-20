class Zoo(object):
    
    def __init__(self, capacity, name):
      self._capacity = capacity
      self._name = name
      self._enclosures = []

    @property
    def capacity(self):
      return self._capacity

    @property
    def name(self):
      return self._name

    @name.setter
    def name(self, name):
      self._name = name

    def add_enclosure(self, enclosure):
      self._enclosures.append(enclosure)

    def number_of_enclosures(self):
      return len(self._enclosures)