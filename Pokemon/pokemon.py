class Pokemon:
    def __init__(self, nombre, defensa, ataque, tipo="N/A"):
        self.nombre = nombre
        self.defensa = defensa
        self.ataque = ataque
        self.tipo = tipo

    def __str__(self):
        return f"{self.nombre} ({self.tipo})"
