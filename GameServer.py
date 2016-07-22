import socket
from juego import Baraja
from juego import Jugador

listaIPs = []
listaJugadores = []

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
        address = address[0]                
        print ("======================")        
        data = data.decode("utf-8")
        jugador = Jugador(data, address)
        listaJugadores.append(jugador)        
        #print (jugador.nombre, jugador.ip)
        '''if data:
            print(data)
            print(numSockets)
            sent = sock.sendto(data, address)'''

def startGame():
    #commands
    print(listaIPs[0])
    print(listaIPs[1])
    print(listaIPs[2])
    print(listaIPs[3])


def reparte_inicial():
    for i in range(4):
        for jugador in listaJugadores:
            carta = baraja.reparteCarta()
            jugador.anade_carta(carta)
	
    for jugador in listaJugadores:
        jugador.muestra_mano()
	
    conexion()
    startGame()

conexion()
reparte_inicial()