import pickle
import os
from tarea import Tarea
from persona import Persona


def main():
    tareas = cargar_tareas()
    personas = cargar_personas()

    opcion = menu()

    while opcion != 9:
        if opcion == 1:
            print("Agregando persona...")
            nombre = input("Ingrese el nombre de la persona: ")
            edad = int(input("Ingrese la edad de la persona: "))
            # Buscamos el id más alto
            id = 0
            for persona in personas:
                if persona.id > id:
                    id = persona.id
            id += 1
            persona = Persona(id, nombre, edad)
            personas.append(persona)
            print(f"Persona agregada: {persona}")
        elif opcion == 2:
            print("Listando personas...")
            for persona in personas:
                print(persona)
        elif opcion == 3:
            print("Agregando tarea...")
            descripcion = input("Ingrese la descripción de la tarea: ")
            responsable = int(input("Ingrese el id del responsable: "))
            for persona in personas:
                if persona.id == responsable:
                    # Buscamos el id más alto
                    id = 0
                    for tarea in tareas:
                        if tarea.id > id:
                            id = tarea.id
                    id += 1

                    tarea = Tarea(id, descripcion, persona)
                    tareas.append(tarea)
                    print(f"Tarea agregada: {tarea}")
                    break
            else:
                print("No se encontró una persona con ese id.")
                print("No se pudo agregar la tarea.")
        elif opcion == 4:
            print("Listando tareas...")
            for tarea in tareas:
                print(tarea)
        elif opcion == 5:
            print("Completando tarea...")
            tarea_id = int(input("Ingrese el id de la tarea: "))
            for tarea in tareas:
                if tarea.id == tarea_id:
                    tarea.cambiar_estado()
                    print(f"Tarea Actualizada: {tarea}")
                    break
            else:
                print("No se encontró una tarea con ese id")

        input("Presione ENTER para continuar...")
        opcion = menu()

    print("Saliendo...")
    guardar_tareas(tareas)
    guardar_personas(personas)


def menu():
    # Limpiamos la pantalla
    os.system("cls")
    print("MENU PRINCIPAL")
    print("1. Agregar Persona")
    print("2. Listar Personas")
    print("3. Agregar Tarea")
    print("4. Listar Tareas")
    print("5. Cambiar Estado de Tarea")
    print("9. Salir")

    while True:
        try:
            opcion = int(input("Ingrese una opción: "))
            if opcion not in [1, 2, 3, 4, 5, 9]:
                print("Ingrese una opción válida: ")
                continue
            return opcion
        except ValueError:
            print("Por favor, ingrese un número entero válido.")


def guardar_tareas(tareas):
    directorio = os.path.dirname(__file__)
    archivo_destino = os.path.join(directorio, "tareas.bin")
    with open(archivo_destino, "wb") as archivo:
        pickle.dump(tareas, archivo)


def cargar_tareas():
    directorio = os.path.dirname(__file__)
    archivo_origen = os.path.join(directorio, "tareas.bin")
    try:
        with open(archivo_origen, "rb") as archivo:
            tareas = pickle.load(archivo)
    except FileNotFoundError:
        tareas = []

    return tareas


def guardar_personas(personas):
    directorio = os.path.dirname(__file__)
    archivo_destino = os.path.join(directorio, "personas.bin")
    with open(archivo_destino, "wb") as archivo:
        pickle.dump(personas, archivo)


def cargar_personas():
    directorio = os.path.dirname(__file__)
    archivo_origen = os.path.join(directorio, "personas.bin")
    try:
        with open(archivo_origen, "rb") as archivo:
            personas = pickle.load(archivo)
    except FileNotFoundError:
        personas = []

    return personas


if __name__ == "__main__":
    main()
