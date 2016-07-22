import socket
import sys

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('192.168.10.11', 10000)
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

finally:
    #sock.close()
    print("message sent")

