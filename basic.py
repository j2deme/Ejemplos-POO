def main():
    print("Jaime Delgado")
    edad = int(input("Cuantos años tienes?"))

    if edad >= 20:
        print("Buenos días")
    else:
        print("Que onda!")

    limite = 11

    print("Ejemplo de For")
    for x in range(1, limite):
        print(x)

    print("Ejemplo de While")
    x = 0
    while x < 10:
        print(x+1)
        x += 1

    nombres = ["Jaime", "Rigo", "Evelyn", "Mario"]
    print(nombres)

    # nombres.append(input("Dame tu nombre: ")) # Añade al final
    # nombres.insert(2, input("Dame tu nombre:")) # Inserta en la posición 2
    nombres[2] = input("Dame tu nombre: ")  # Reemplaza la posición 2
    print(nombres)

    # print(nombres[2])


if __name__ == "__main__":
    main()
