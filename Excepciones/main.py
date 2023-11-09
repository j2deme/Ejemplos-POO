def main():
  '''
  repite = True
  while repite:
    try:
      a = int(input("Ingresa el número A: "))
      b = int(input("Ingresa el número B: "))
    except ValueError:
      print("Los valores A y B, deben ser enteros")
    else:
      repite = False
  '''
  a = leeEnteros("Ingresa el número A: ")
  b = leeEnteros("Ingresa el número B: ")
  
  repite = True
  while repite:
    try:
      print(divide(a, b))
    except ZeroDivisionError:
      print("No se puede dividir entre cero")
      while b == 0:
        b = leeEnteros("Ingresa el número B: ")
    else:
      repite = False

def divide(a, b):
  # throws ZeroDivisionError
  return a / b

def leeEnteros(etiqueta):
  repite = True
  while repite:
    try:
      x = int(input(etiqueta))
    except ValueError:
      print("El valor debe ser entero")
    else:
      repite = False
      return x

if __name__ == '__main__':
  main()