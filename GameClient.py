import socket
import sys
import os

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('192.168.10.19', 10000)

def recvanddecode():
    data = sock.recvfrom(4096)
    data = data.decode("utf-8")

    return data

def bufandsend():
    message = input()
    sent = sock.sendto(message.encode(), server_address)

    return sent

def inicio():
    try:
        message = input('Que nombre quieres usar: ')
        # Send the name to gameserver
        sent = sock.sendto(message.encode(), server_address)
        # Receive response - print cards in console
        rotaciones = 0
        while rotaciones < 4:
            data, server = sock.recvfrom(4096)
            print(data.decode("utf-8"))
            rotaciones = rotaciones + 1
        data, addr = sock.recvfrom(4096)
        print(data)
        #os.system('clear')

def fase_mus():
            #wait for the server to send data
            print ("Waiting for other players")
            data = recvanddecode()
            if data == "se quiere mus? [mus, corto]":
                #send the response to the server
                sent = bufandsend()
                #if mus there is a new branch
            if sent = "mus"
                #wait until the server ask for the number of cards
                data = recvanddecode();
                if data == "que cartas quieres descartar ?":
                    print("(Separadas por espacios)")
                    sent = bufandsend()
            



def main():
    inicio()
    fase_mus()

main()
