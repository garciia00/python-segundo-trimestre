class Equipo :
    def __init__(self, nom_eq) :
        self.nombre_equipo = nom_eq
class Jugador :
    def __init__(self, dor, nom, eq) :
        self.dorsal = dor
        self.nombre = nom
        self.equipo = eq
    def mostrar(self) :
        print(f"{self.dorsal}.{self.nombre}.{self.equipo.nombre_equipo}")




equipo1 = Equipo("los angeles lakers")
equipo2 = Equipo("FC Barcelona")

jugador1 = Jugador(10,"Messi", equipo1)
jugador2 = Jugador(7,"RickyRubio", equipo2)


jugador1.mostrar()  
jugador2.mostrar()