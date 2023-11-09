from perro import Perro
from gato import Gato
from animal import Animal

def main():
  perro = Perro("Firulais", 5, "Urbano")
  gato = Gato("Garfield", 3, 7)

  perro.comer()
  perro.dormir()
  perro.hacer_sonido()
  print(f'Es cachorro? {perro.es_cachorro()}')

  gato.comer()
  gato.hacer_sonido()
  print(f'Vidas? {gato.vidas}')
  print(f'Sobrevive? {gato.sobrevive()}')
  print(f'Vidas? {gato.vidas}')
  print(f'Sobrevive? {gato.sobrevive()}')
  print(f'Sobrevive? {gato.sobrevive()}')
  print(f'Sobrevive? {gato.sobrevive()}')
  print(f'Sobrevive? {gato.sobrevive()}')
  print(f'Vidas? {gato.vidas}')
  gato.edad = 16
  print(f'Sobrevive? {gato.sobrevive()}')
  print(f'Vidas? {gato.vidas}')
  print(f'Sobrevive? {gato.sobrevive()}')
  print(f'Vidas? {gato.vidas}')

  del gato
  del perro

  pikachu = Animal("Pikachu", 2)
  pikachu.hacer_sonido()
  pikachu.comer()
  pikachu.dormir()
  del pikachu

if __name__ == "__main__":
  main()