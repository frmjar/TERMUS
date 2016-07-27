from random import randint
from random import seed

class Carta(object):
	def __init__(self, numero, palo):
		self.numero = numero
		self.palo = palo
	def __str__(self):
		return self.numero + " de " +  self.palo
		
	def __eq__(self, other):
		if self.numero == "3" and other.numero == "K":
			return True
		else if self.numero == "K" and other.numero == "3":
			return True
		else:
			return self.numero == other.numero
		
	def __gt__(self, other):
	
		figuras = ["J", "Q", "K"]
	
		if not (self.numero in figuras or other.numero in figuras):
			return int(self.numero) > int(other.numero)
		else if self.numero in figuras and not other.numero in figuras:
			if other.numero == "3":
				return False
			else:
				return True
		else if not self.numero in figuras and other.numero in figuras:
			if self.numero == "3":
				if other.numero != "K":
					return True
				else:
					return False
			else:
				return False
		else: 
			if self.numero == "J":
				return False
			elif self.numero == "Q":
				if other.numero == "J"
					return True
				else:
					return False
			elif self.numero == "K":
				if other.numero == "K":
					return False
				else:
					return True
				
	def __st__(self, other):
		if not (self.numero in figuras or other.numero in figuras):
			return int(self.numero) < int(other.numero)
		else if self.numero in figuras and not other.numero in figuras:
			if other.numero == "3":
				if self.numero == "K"
					return False
				else:
					return True
		else if not self.numero in figuras and other.numero in figuras:
			if self.numero == "3":
				return False
		else: 
			if self.numero == "J":
				if other.numero == "J":
					return False
				else:
					return True
			elif self.numero == "Q":
				if other.numero == "K"
					return True
				else:
					return False
			elif self.numero == "K":
				return False
			

class Baraja(object):
	
	cartas_repartidas = []
	numeros = ["1", "2", "3", "4", "5", "6", "7", "J", "Q", "K"]
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
		for carta in self.cartas_repartidas:
			str(carta)
	
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
			
			
			