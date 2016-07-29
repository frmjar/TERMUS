import socket
from juego import Baraja
from juego import Jugador

listaIPs = []
listaJugadores = []
fase1 = ["mus", "corto"]
fase2 = ["envido", "paso"]
fase3 = ["envido", "paso"]
fase4 = ["si", "no", "envido", "paso"]
fase5 = ["si", "no"]

baraja = Baraja()

def conexion():
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to the port
    server_address = ('192.168.10.11', 10000)
    sock.bind(server_address)

    while True and len(listaJugadores) < 4:
        data, address = sock.recvfrom(4096)
        listaIPs.append(address)        
        print ("======================")        
        data = data.decode("utf-8")
        jugador = Jugador(data, address)
        listaJugadores.append(jugador)
        
    return sock


def startGame():
    #commands
    print(listaIPs[0])
    print(listaIPs[1])
    print(listaIPs[2])
    print(listaIPs[3])


def reparte_inicial(sock):
    for i in range(4):
        for jugador in listaJugadores:
            carta = baraja.reparteCarta()
            jugador.anade_carta(carta)
	
    for jugador in listaJugadores:
        jugador.muestra_mano(sock)
		
'''def fase_mus():
	mus = Yes	
	while mus:
		for x in listaJugadores:
'''		

def main():

    sock = conexion()
    reparte_inicial(sock)    


main()













