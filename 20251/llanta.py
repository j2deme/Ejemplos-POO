class Llanta:
    def __init__(self, etiqueta):
        self.etiqueta = etiqueta
        self.presion = 0

    def inflar(self, presion=32):
        self.presion = presion
        print(f"Inflando la llanta {self.etiqueta} a {self.presion} PSI")

    def __str__(self):
        return f"Llanta: {self.etiqueta} ({self.presion} PSI)"
