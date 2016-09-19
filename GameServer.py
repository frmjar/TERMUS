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
    server_address = ('192.168.10.19', 10000)
    sock.bind(server_address)
    #refuse > 4 connections

    while True and len(listaJugadores) < 4:
        data, address = sock.recvfrom(4096)
        print ("Esperando nueva conexion...")        
        data = data.decode("utf-8")
        jugador = Jugador(data, address)
        listaJugadores.append(jugador)
        print ('Conexión establecida con ' + jugador.nombre)
        
    return sock

def reparte_inicial(sock):
    for i in range(4):
        for jugador in listaJugadores:
            carta = baraja.reparteCarta()
            jugador.anade_carta(carta)
	
    for jugador in listaJugadores:
        jugador.muestra_mano(sock)

def reparte_cartas(jugador,num,sock):
    for i in range(num):

		
def fase_mus(sock):
    cont = 0
    while True:
        enviarMensaje(listaJugadores[cont].address,"'\n' se quiere mus? [mus, corto]'\n'",sock)
        data,address = sock.recvfrom(4096)
        data = data.decode("utf-8")

        if data == fMus[1]:
            return
        else if data == fMus[0]:
            cont = cont + 1
            enviarMensaje(listaJugadores[cont].address,"'\n' que cartas quieres descartar ?'\n'",sock)
            data,address = sock.recvfrom(4096)
            data = data.decode("utf-8")
            data.split(' ')
            listaJugadores[cont].descarte = data

        if cont > 3 :
            cont = 0
            for i in range (4):
                enviarMensaje(listaJugadores[i].address,"repartiendo " + listaJugadores[i].descarte ,sock)
                reparte_cartas(i,listaJugadores[i].descarte,sock)


def enviarMensaje(ip, msg, sock):
    sock.sendto(msg.encode(), ip)

def main():

    sock = conexion()
    reparte_inicial(sock)    
    fase_mus(sock)

main()













