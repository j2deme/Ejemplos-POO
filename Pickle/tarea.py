from persona import Persona


class Tarea:
    def __init__(self, id, descripcion, responsable: Persona):
        self.id = id
        self.descripcion = descripcion
        self.completada = False
        self.responsable = responsable

    def __str__(self):
        icono = "✅" if self.completada else "❌"
        return f"{self.id}: {self.descripcion} ({icono}) @{self.responsable.nombre}"

    def cambiar_estado(self):
        self.completada = not self.completada
