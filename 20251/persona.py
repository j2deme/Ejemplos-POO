class Persona:
    __nombre = ""
    __edad = 0

    def saludar(self):
        print(f"Hola, soy {self.getNombre()}")

    # Getters & Setters
    def setNombre(self, nombre):
        if not nombre == "":
            self.__nombre = nombre.upper()

    def getNombre(self):
        return self.__nombre

    def setEdad(self, year):
        self.__edad = 2025 - year


# ======

persona1 = Persona()
persona1.setNombre("jaime")
persona1.saludar()

persona1.setEdad(1987)
# print(persona1.edad)
# print(persona1)

persona2 = Persona()
persona2.setNombre("SaNdY")
persona2.saludar()
# print(persona2)
