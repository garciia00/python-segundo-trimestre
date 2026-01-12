class Equipo:
    def __init__(self, nom_eq):
        self.nombre_equipo = nom_eq
        self.jugadores_eq = []
    
    def anyadir_jugador(self, jugador):
        self.jugadores_eq.append(jugador)


class Jugador:
    def __init__(self, dor, nom):
        self.dorsal = dor
        self.nombre = nom
        self.equipo = None

    def anyadir_equipo(self, equipo):
        self.equipo = equipo
        equipo.anyadir_jugador(self)

    def mostrar(self):
        print(f"{self.dorsal}. {self.nombre}")


equipo1 = Equipo("Barça")
equipo2 = Equipo("Real Madrid")

jugador1 = Jugador(11, "Raphinha")
jugador2 = Jugador(7, "Vini")
jugador3 = Jugador(25, "Mijatovic")
jugador4 = Jugador(12, "Marcelo")

jugador1.anyadir_equipo(equipo1)
jugador2.anyadir_equipo(equipo2)
jugador3.anyadir_equipo(equipo2)
jugador4.anyadir_equipo(equipo2)

print(f"Equipo: {equipo2.nombre_equipo}")
for jugador in equipo2.jugadores_eq:
    jugador.mostrar()
