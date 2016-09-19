import socket
import sys
import os

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('192.168.10.19', 10000)

def inicio():
    try:
        message = input('Que nombre quieres usar: ')
        # Send data
        sent = sock.sendto(message.encode(), server_address)
        # Receive response
        rotaciones = 0
        while rotaciones < 4:
            data, server = sock.recvfrom(4096)
            print(data.decode("utf-8"))
            rotaciones = rotaciones + 1
        data, addr = sock.recvfrom(4096)
        print(data)
        #os.system('clear')
    finally:
        print("fase de repartir terminada \n")

def fase_mus():
        sock.recvfrom(4096)
        message = input()
        sent = sock.sendto(message.encode(),server_address)
        sock.recvfrom(4096)
        message = input()
        sent = sock.sendto(message.encode(),server_address)

def main():
    inicio()
    fase_mus()
    while true:
        data, addr = sock.recvfrom(4096)
main()
