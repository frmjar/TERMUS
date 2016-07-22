import socket

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('192.168.10.11', 10000)

#Mensaje de conexion al servidor.
sent = sock.sendto(bytes([1]), server_address)
try:
   	while True:
        #print(sock.getpeername())
        message = input('Que nombre quieres usar: ')
        sent = sock.sendto(message.encode(), server_address)
        # Receive response
        data, server = sock.recvfrom(4096)

        #print(data)
finally:
    #sock.close()
    print("message sent")

