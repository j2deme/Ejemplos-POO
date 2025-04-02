from pokemon import Pokemon


class TipoElectrico(Pokemon):
    def __init__(self, nombre, defensa, ataque):
        super().__init__(nombre, defensa, ataque, "Eléctrico")
