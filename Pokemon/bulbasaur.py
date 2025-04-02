from hierba import TipoHierba
from venenoso import TipoVenenoso


class Bulbasaur(TipoHierba, TipoVenenoso):
    def __init__(self, defensa=111, ataque=118):
        TipoHierba.__init__(self, "Bulbasaur", defensa, ataque)
        TipoVenenoso.__init__(self, "Bulbasaur", defensa, ataque)
        self.tipo = "Hierba / Venenoso"

    def __str__(self):
        return f"{self.nombre} ({self.tipo}) 🌱 / ☠️"
