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
		elif self.numero == "K" and other.numero == "3":
			return True
		elif self.numero == "1" and other.numero == "2":
			return True
		elif self.numero == "2" and other.numoer == "1":
			return True
		else:
			return self.numero == other.numero
		
	def __gt__(self, other):
	
		figuras = ["J", "Q", "K"]
	
		if not (self.numero in figuras or other.numero in figuras):
			return int(self.numero) > int(other.numero)
		elif self.numero in figuras and not other.numero in figuras:
			if other.numero == "3":
				return False
			else:
				return True
		elif not self.numero in figuras and other.numero in figuras:
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
				if other.numero == "J":
					return True
				else:
					return False
			elif self.numero == "K":
				if other.numero == "K":
					return False
				else:
					return True

	def __ge__(self, other):
		return self > other or self == other

	def __lt__(self, other):

		figuras = ["J", "Q", "K"]

		if not (self.numero in figuras or other.numero in figuras):
			return int(self.numero) < int(other.numero)
		elif self.numero in figuras and not other.numero in figuras:
			if other.numero == "3":
				if self.numero == "K":
					return False
				else:
					return True
		elif not self.numero in figuras and other.numero in figuras:
			if self.numero == "3":
				return False
			else:
				return True
		else: 
			if self.numero == "J":
				if other.numero == "J":
					return False
				else:
					return True
			elif self.numero == "Q":
				if other.numero == "K":
					return True
				else:
					return False
			elif self.numero == "K":
				return False

	def __le__(self, other):
		return self < other or self == other
			

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
			print (carta)
	
class Jugador(object):	

	def __init__(self, nombre, address):
		self.nombre = nombre
		self.mano = []
		self.puntos = 0
		self.address = address	
		self.descarte = []
		
	def suma_puntos(self, puntos):
		self.puntos = self.puntos + puntos	
	
	def anade_carta(self, carta):
		self.mano.append(carta)
		if len(self.mano) == 4:
			self.mano.sort()

	def eliminar_carta(self,posicion):
		self.mano.pop(posicion)

	def muestra_mano(self, sock):
		print ("Mano de " + self.nombre + ": ")
		for carta in self.mano:
			cartas = str(carta)		
			print(self.address)	
			sent = sock.sendto(str.encode("++++++++++++++/++++++++++++++"), self.address)
			sent = sock.sendto(cartas.encode(), self.address)
			sent = sock.sendto(str.encode("++++++++++++++/++++++++++++++"), self.address)



carta1 = Carta("3", "Bastos")
carta2 = Carta("3", "Espadas")
carta3 = Carta("2", "Bastos")
carta4 = Carta("Q", "Bastos")
carta9 = Carta("J", "asf")
carta10 = Carta("1", "asd")
carta5 = Carta("Q", "Espadas")
carta6 = Carta("K", "Bastos")

