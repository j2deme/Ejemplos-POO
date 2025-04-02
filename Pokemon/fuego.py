from pokemon import Pokemon


class TipoFuego(Pokemon):
    def __init__(self, nombre, defensa, ataque, tipo="Fuego"):
        super().__init__(nombre, defensa, ataque, tipo)
