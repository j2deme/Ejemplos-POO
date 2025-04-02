from electrico import TipoElectrico


class Pikachu(TipoElectrico):
    def __init__(self, defensa=50, ataque=55):
        super().__init__("Pikachu", defensa, ataque)
