class Coche:
    __velocidad = 0
    __marcha = 0
    __luces = False

    def __init__(self, luces=False):
        self.__luces = luces
        self.llantas = []

    def acelerar(self):
        self.__velocidad += 10

    def frenar(self):
        self.__velocidad -= 10

    def cambiarMarcha(self, marcha):
        self.__marcha = marcha

    def encenderLuces(self):
        self.__luces = True

    def encender(self, motor: 'Motor') -> None:
        motor.encender()

    def agregarLlanta(self, llanta):
        if len(self.llantas) < 4:
            self.llantas.append(llanta)

    def __str__(self):
        return f"Velocidad: {self.__velocidad}, Marcha: {self.__marcha}, Luces: {self.__luces}"
