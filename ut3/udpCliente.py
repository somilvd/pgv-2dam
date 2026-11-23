import socket, sys

ip_server=sys.argv[1]

port_server=int(sys.argv[2])

cliente=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

servidor=(ip_server, port_server)
cliente.connect(servidor)

while True:
    mensaje=input("Mensaje para enviar: ")
    socket.sendto(mensaje.encode('utf-8'), servidor)
    respuesta=cliente.recvfrom(1024)
    print(respuesta.decode('utf-8'))

