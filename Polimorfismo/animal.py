from abc import ABC, abstractmethod
from mixinMortalidad import MixinMortalidad

class Animal(ABC, MixinMortalidad):

  def __init__(self, nombre="", edad=1):
    self.nombre = nombre
    self.edad = edad
  
  @abstractmethod
  def comer(self):
    pass

  def dormir(self):
    if self.nombre == '':
      print("El animal está durmiendo 💤")
    else:
      print(f"{self.nombre} está durmiendo 💤")