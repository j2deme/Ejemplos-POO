from mamifero import Mamifero
from oviparo import Oviparo

class Ornitorrinco(Mamifero, Oviparo):
  
  def __init__(self, nombre="", edad=1):
    super().__init__(nombre, edad)
    self.NUMERO_HUEVOS = 0

  def comer(self):
    print("El ornitorrinco está comiendo 🐞🐛🐚")

  def morir(self):
    print("Oh! me muero! 😵")