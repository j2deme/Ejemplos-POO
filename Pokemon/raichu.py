from electrico import TipoElectrico


class Raichu(TipoElectrico):
    def __init__(self, defensa=60, ataque=90):
        super().__init__("Raichu", defensa, ataque)
