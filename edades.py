def main():
    edades = []

    for i in range(0, 5):
        edad = int(input("Edad: "))
        edades.append(edad)

    edades.sort()
    print(edades)


if __name__ == "__main__":
    main()
