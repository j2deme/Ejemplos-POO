from oviparo import Oviparo
from animal import Animal


class Pinguino(Animal, Oviparo):
  def comer(self):
    print("El pingüino está comiendo 🐟🍣")