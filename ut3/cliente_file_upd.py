import socket, sys

cliente=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip=sys.argv[1]
puerto=int(sys.argv[2])
archivo=sys.argv[3]

fichero=open(archivo,'rb')

while True:
    datos=fichero.read(1024)
    if not datos:
        #Datagrama sin payload => vacio
        print("salimos")
        cliente.sendto(b"",(ip, puerto))
        fichero.close()
        cliente.close()
        break
    cliente.sendto(datos, (ip, puerto))
print("Fin bucle")