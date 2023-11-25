class Persona:
    def __init__(self, id, nombre, edad):
        self.id = id
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return "{} - {} ({})".format(self.id, self.nombre, self.edad)
