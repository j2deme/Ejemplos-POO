from ContadorPasos import ContadorPasos


def main():
    miContador = ContadorPasos()
    print(miContador.pasos)

    distancia1 = int(input("¿Que distancia vas a caminar?"))
    pasos1 = miContador.calcularPasos(distancia1)
    print("Para caminar", distancia1, "metros, se ocupan", pasos1, "pasos")

    for i in range(0, pasos1):
        miContador.contar()  # type: ignore

    print(miContador.pasos)

    miContador.contar(5) # type: ignore
    print(miContador.pasos)

    miContador.contar(7, 2)
    print(miContador.pasos)

    # pasos2 = int(input("Pasos? "))
    # distancia2 = miContador.calcularDistancia(pasos2)
    # print("Caminar", pasos2, "pasos, nos permite avanzar", distancia2, "metros")

    print("SOBRECARGA DE OPERADORES")

    cuenta1 = ContadorPasos(10)
    cuenta2 = ContadorPasos(20)
    cuenta3 = cuenta1 + cuenta2
    cuenta2 = cuenta2 - cuenta1

    print(cuenta3)
    print(cuenta2)


if __name__ == "__main__":
    main()
