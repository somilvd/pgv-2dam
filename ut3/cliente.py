import socket, sys

cliente=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente.connect((sys.argv[1],int(sys.argv[2])))

a=input("Qué enviamos? ")
cliente.sendall(a.encode('utf-8'))

respuesta=cliente.recv(1024)

print(respuesta.decode('utf-8'))
cliente.close()