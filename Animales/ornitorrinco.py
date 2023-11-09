from mamifero import Mamifero
from oviparo import Oviparo
from venenoso import Venenoso

class Ornitorrinco(Mamifero, Oviparo, Venenoso):
  
  def __init__(self, nombre, edad):
    super().__init__(nombre, edad)
    self.NUMERO_HUEVOS = 0