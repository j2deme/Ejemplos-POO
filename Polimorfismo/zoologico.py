from animal import Animal
from mamifero import Mamifero


class Zoologico:
  def __init__(self):
    self.animales = []

  def agregar_animal(self, animal: Animal):
    self.animales.append(animal)
  
  def alimentar_animales(self):
    for animal in self.animales:
      animal.comer()
      if isinstance(animal, Mamifero):
        animal.amamantar()

  def hora_dormir(self):
    for animal in self.animales:
      animal.dormir()

  def nacen_animales(self):
    for animal in self.animales:
      if isinstance(animal, Mamifero):
        animal.parir()
      else:
        animal.poner_huevo()