from perro import Perro
from gato import Gato
from leon import Leon
from ornitorrinco import Ornitorrinco
from pinguino import Pinguino
from animal import Animal
from zoologico import Zoologico

def main():
  lomito = Perro(nombre="Oddie")
  michi = Gato(nombre="Garfield")
  alex = Leon(nombre="Alex")
  perry = Ornitorrinco(nombre="Perry")
  kobalski = Pinguino(nombre="Kobalski")
  # animal = Animal() # No se puede instanciar una clase abstracta

  lomito.comer()
  lomito.dormir()

  michi.comer()
  michi.dormir()

  print("== EJEMPLO ==")

  # Uso del polimorfismo
  # Mediante el uso del polimorfismo, podemos crear una lista de objetos de diferentes clases
  # que heredan de la misma clase padre y en consecuencia, pueden ser tratados de la misma manera
  animales = [lomito, michi, alex, perry]

  for animal in animales:
    animal.comer() # Método sobreescrito
    animal.dormir() # Método heredado
    animal.morir() # Método del Mixin

  print("== ZOO ==")
  zoo = Zoologico()

  zoo.agregar_animal(lomito)
  zoo.agregar_animal(michi)
  zoo.agregar_animal(alex)
  zoo.agregar_animal(perry)
  zoo.agregar_animal(kobalski)

  zoo.alimentar_animales()
  zoo.hora_dormir()
  zoo.nacen_animales()

if __name__ == "__main__":
  main()