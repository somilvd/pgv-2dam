import socket

servidor=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

servidor.bind(("",4444))
clientes={}

while True:
    datos, addr = servidor.recvfrom(65536)
    if addr in clientes:
        print("Cliente existente")
    else:
        print("Cliente nuevo")
        clientes[addr]=datos
    for cli in clientes:
        if cli != addr:
            servidor.sendto(f"{cli}: {datos.encode('utf-8')}".encode('utf-8'),cli)
