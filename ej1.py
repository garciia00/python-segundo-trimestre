class jugador :
    def __init__(self, dor, nom) :
        self.dorsal = dor
        self.nombre = nom
    def mostrar(self) :
        print(f"{self.dorsal}.{self.nombre}")

jugador1= jugador(10,"Messi")
jugador2= jugador(7,"RickyRubio")


jugador1.mostrar()  
jugador2.mostrar()