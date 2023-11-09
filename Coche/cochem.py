class Coche:
  def __init__(self):
    self.llantas = []
    
  def encender(self, motor):
    motor.encender()
  
  def agregarLlanta(self, llanta):
    self.llantas.append(llanta)