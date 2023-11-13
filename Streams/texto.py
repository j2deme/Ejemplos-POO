import os


def main():
    # Obtenemos el directorio del archivo actual
    directorio = os.path.dirname(__file__)

    # Unimos el directorio actual con el nombre de los archivos
    # Esto nos da la ruta completa al archivo de origen y al archivo de destino
    archivo_origen = os.path.join(directorio, "numeros.txt")
    archivo_destino = os.path.join(directorio, "salida.txt")

    # Abrimos el archivo de origen en modo de lectura
    with open(archivo_origen, "r") as origen:
        # Abrimos el archivo de destino en modo de escritura
        with open(archivo_destino, "w") as destino:
            while True:
                # Leemos un caracter del archivo de origen
                caracter = origen.read(1)
                if not caracter:
                    break

                try:
                    num = int(caracter)
                    destino.write(str(num * 2))
                except ValueError:
                    destino.write(caracter)


if __name__ == "__main__":
    main()
