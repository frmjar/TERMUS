import socket
from juego import Baraja
from juego import Jugador

listaJugadores = []
fMus = ["mus", "corto"]
fGrande = ["envido", "paso"]
fChica = ["envido", "paso"]
fPares = ["si", "no", "envido", "paso"]
fJuego = ["si", "no", "envido", "paso"]
fPunto = ["envido", "paso"]

baraja = Baraja()

def conexion():
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to the port
    server_address = ('192.168.10.11', 10000)
    sock.bind(server_address)

    while True and len(listaJugadores) < 4:
        data, address = sock.recvfrom(4096)
        print ("======================")        
        data = data.decode("utf-8")
        jugador = Jugador(data, address)
        listaJugadores.append(jugador)
        
    return sock

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

def enviarMensaje(ip, msg, sock):
    sock.sendto(msg.encode(), ip)

def main():

    sock = conexion()
    reparte_inicial(sock)    
    enviarMensaje(listaJugadores[0].address, "testing send", sock)

main()













