from fuego import TipoFuego


class Charmander(TipoFuego):
    def __init__(self, defensa=60, ataque=65):
        super().__init__("Charmander", defensa, ataque)
