from motor import Motor
from llanta import Llanta
from cochem import Coche as CocheMetodos
from cochea import Coche as CocheAtributos

def main():
  ejemploCocheMetodos()
  ejemploCocheAtributos()

def ejemploCocheMetodos():
  print("Composición por Métodos")
  motor = Motor("4569")
  coche = CocheMetodos()
  coche.encender(motor)

  fi = Llanta("Frontal Izq")
  fi.inflar(28)
  fd = Llanta("Frontal Der")
  fd.inflar(28)

  coche.agregarLlanta(fi)
  coche.agregarLlanta(fd)

  print(coche.llantas[0])

def ejemploCocheAtributos():
  print("Composición por atributos")
  coche = CocheAtributos("ABCDE")
  coche.encender()
  coche.inflarRuedas()

  print(coche.ruedas[2])


if __name__ == "__main__":
  main()