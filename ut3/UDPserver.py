import socket

servidor=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

servidor.bind(("",4444))

while True
    datos, addr = servidor.recvfrom(1024)

print(addr)