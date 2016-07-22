from random import randint
from random import seed

class Carta(object):
	def __init__(self, numero, palo):
		self.numero = numero
		self.palo = palo
	def devuelve_carta(self):
		return self.numero + " de " +  self.palo

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
			x.devuelve_carta()
	
class Jugador(object):	

	def __init__(self, nombre, address):
		self.nombre = nombre
		self.mano = []
		self.puntos = 0
		self.address = address	
	def suma_puntos(self, puntos):
		self.puntos = self.puntos + puntos
	
	
	def anade_carta(self, carta):
		self.mano.append(carta)	

	def muestra_mano(self, sock):
		print ("Mano de " + self.nombre + ": ")
		for carta in self.mano:
			cartas = carta.devuelve_carta()		
			print(self.address)	
			sent = sock.sendto(cartas.encode(), self.address)
			
			
'''class tapete():

	commandos = [envido, mus, fadsfads]
	fase1  
'''









