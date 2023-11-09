from multipledispatch import dispatch


class ContadorPasos:
    pasos = -1

    def __init__(self, pasos=0):
        self.pasos = pasos

    def __del__(self):
        pass
        # print("Termine con", self.pasos, "pasos")

    @dispatch()
    def contar(self): # type:ignore
        self.pasos += 1

    @dispatch(int)
    def contar(self, pasos): # type: ignore
        self.pasos += pasos

    @dispatch(int, int)
    def contar(self, pasos, saltos):
        self.pasos += pasos + (2 * saltos)

    def saltarAdelante(self):
        self.contar() # type:ignore
        self.contar() # type:ignore

    # Toma la cantidad de pasos y devuelve la distancia en metros
    def calcularDistancia(self, pasos):
        # 1m = 0.7 pasos
        return pasos * 0.7

    # Toma la distancia en metros y devuelve la cantidad de pasos
    def calcularPasos(self, distancia):
        return round(distancia / 0.7)

    def __add__(self, cuenta):
        return ContadorPasos(self.pasos + cuenta.pasos)
    
    def __sub__(self, cuenta):
        return ContadorPasos(self.pasos - cuenta.pasos)
    
    def getPasos(self):
        return self.pasos
    
    def __str__(self):
        return str(self.pasos) + " 👟"