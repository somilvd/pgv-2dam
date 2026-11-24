import socket

servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

servidor.bind(("", 4444))

archivo=open("fichero", "wb")

while True:
    datos, addr = servidor.recvfrom(65536) #BLOQUEANTE
    archivo.write(datos)