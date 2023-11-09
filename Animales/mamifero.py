from animal import Animal

class Mamifero(Animal):
  def __init__(self, nombre, edad, especie="Mamífero"):
    super().__init__(nombre, edad)
    self.especie = especie

  def amamantar(self):
    print("🍼")

  def parir(self):
    print("👶🏻")