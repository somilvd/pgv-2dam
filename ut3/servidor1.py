import socket

#Socket de escucha en IPv4 + TCP
servidor=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

servidor.bind(("0.0.0.0",4444))
servidor.listen()
a=input("Aquí esperando")