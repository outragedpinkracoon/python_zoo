class Animal(object):

  def __init__(self, kind):
    self._kind = kind
    self._edible_animals = []
  
  @property
  def kind(self):
    return self._kind

  def add_edible(self, edible_animal):
    self._edible_animals.append(edible_animal)
  
  def eats(self, food_type):
    for edible_animal_kind in self._edible_animals:
      if edible_animal_kind.lower() == food_type.lower():
        return True
    return False
  
  @property
  def edible_animals(self):
      return self._edible_animals
  
