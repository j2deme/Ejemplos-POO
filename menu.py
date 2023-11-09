def main():
  salir = False

  while not salir:
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("9. Salir")

    opcion = int(input("Elige tu opción"))

    if opcion < 9:
      print (opcion)
    elif opcion == 9:
      salir = True

if __name__ == "__main__":
  main()