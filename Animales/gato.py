from animal import Animal

class Gato(Animal):
  def __init__(self, nombre, edad, vidas):
    super().__init__(nombre, edad)
    self.vidas = vidas

  def hacer_sonido(self):
    super().hacer_sonido()
    print("Miau! 🐈")
    #print(f'{self.nombre} esta maullando')
  
  def sobrevive(self):
    if self.edad > 15 or self.vidas > 1:
      self.vidas -= 1
      self.edad = 1
    
    return self.vidas > 0
  
  def __del__(self):
    print(f'{self.nombre} se fue al cielo de los gatos')