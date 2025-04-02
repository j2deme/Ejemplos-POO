from animal import Animal


class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza

    def hacer_sonido(self):
        # print(f'{self.nombre} esta ladrando')
        # super().hacer_sonido()
        print("Guau! 🐕")

    def es_cachorro(self):
        return self.edad < 2

    '''def __del__(self):
        print(f'{self.nombre} se fue al cielo de los perros')'''
