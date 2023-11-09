from motor import Motor
from llanta import Llanta

class Coche:
  def __init__(self, no_serie):
    self.motor = Motor(no_serie)
    self.ruedas = [
      Llanta("FI"), Llanta("FD"),
      Llanta("TI"), Llanta("TD")
    ]

  def encender(self):
    self.motor.encender()

  def inflarRuedas(self):
    for llanta in self.ruedas:
      llanta.inflar()