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

def reparte_cartas(jugador,sock):
    for i in jugador.descarte:
        jugador.eliminar_carta(i)
        carta = baraja.reparteCarta()
        jugador.anade_carta(carta)
    
		
def fase_mus(sock):
    cont = 0
    while True:
        #send the message to all players
        enviarMensaje(listaJugadores[cont].address,"se quiere mus? [mus, corto]",sock)
        data,address = sock.recvfrom(4096)
        data = data.decode("utf-8")
        #decode if mus or corto
        #if corto send to all players who has done it
        if data == fMus[1]:
            for j in range(4)
                if j != cont:
                    enviarMensaje(listaJugadores[j].address,"Jugador " +  listaJugadores[j].nombre + " Ha cortado el mus",sock)
            return
        #otherwhise continue asking
        elif data == fMus[0]:
            cont = cont + 1
            print (cont)

        #if all players have been asked and said yes, reparte cartas and do it all over again
        if cont > 3 :
            cont = 0
            for i in range(4):
                enviarMensaje(listaJugadores[i].address,"que cartas quieres descartar ?",sock)
                data,address = sock.recvfrom(4096)
                data = data.decode("utf-8")
                data.split(' ')
                print(data)
                listaJugadores[i].descarte = data
                enviarMensaje(listaJugadores[i].address,"repartiendo " +  len(listaJugadores[i].descarte) + " cartas",sock)
                reparte_cartas(listaJugadores[i],sock)
                listaJugadores[i].muestra_mano(sock)


def enviarMensaje(ip, msg, sock):
    sock.sendto(msg.encode(), ip)

def main():

    sock = conexion()
    reparte_inicial(sock)    
    fase_mus(sock)

main()













