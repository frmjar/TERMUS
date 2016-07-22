from random import randint
from random import seed

class Carta(object):
	def __init__(self, numero, palo):
		self.numero = numero
		self.palo = palo
	def imprime_carta(self):
		print "%s de %s" % (self.numero, self.palo)

class Baraja(object):
	
	cartas_repartidas = []
	numeros = ["1", "2", "3", "4", "5", "6", "7","J", "Q", "K"]
	palos = ["Bastos", "Oros", "Copas", "Espadas"]
	
	def __init__(self):
		pass

	def reparteCarta(self):
		
		salte = False
		
		while not salte:
	
			seed()
			ran_int = randint(0,len(self.numeros)-1)
			ran_palo = randint(0,len(self.palos)-1)	
			numero = self.numeros[ran_int]
			palo = self.palos[ran_palo]
			carta = Carta(numero, palo)
			existe_carta = False
		
			for cartas in self.cartas_repartidas:
				if numero == cartas.numero and palo == cartas.palo:
					existe_carta = True
					break				
		
			if not existe_carta:
				self.cartas_repartidas.append(carta)
				salte=True

		return carta 

	def muestraCartasRepartidas(self):
		for x in self.cartas_repartidas:
			x.imprime_carta()
	
class Jugador(object):	

	def __init__(self, nombre):
		self.nombre = nombre
		self.mano = []
		self.puntos = 0
	
	def suma_puntos(self, puntos):
		self.puntos = self.puntos + puntos
	
	
	def anade_carta(self, carta):
		self.mano.append(carta)	

	def muestra_mano(self):
		print "Mano de " + self.nombre + ": "
		for carta in self.mano:
			carta.imprime_carta()
			

jugador1 = Jugador("Fernando")
jugador2 = Jugador("Javier")
jugador3 = Jugador("Marta")
jugador4 = Jugador("Felix")

jugadores = [jugador1, jugador2, jugador3, jugador4]

baraja = Baraja()

def reparte_inicial():
	for i in range(4):
		for jugador in jugadores:
			carta = baraja.reparteCarta()
			jugador.anade_carta(carta)
		
reparte_inicial()

for jugador in jugadores:
	jugador.muestra_mano()


'''baraja.muestraCartasRepartidas()'''







class tapete():

	commandos = [envido, mus, fadsfads]
	fase1  










