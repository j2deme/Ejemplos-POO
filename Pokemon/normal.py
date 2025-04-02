from pokemon import Pokemon


class TipoNormal(Pokemon):
    def __init__(self, nombre, defensa, ataque):
        super().__init__(nombre, defensa, ataque, "Normal")

    def __str__(self):
        return "🔘"
