import socket

# IPv4 + TCP
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Interfaz del puerto
servidor.bind(("0.0.0.0", 4444))
# Apertura del puerto
servidor.listen()
# Y ahora viene TCP
# Esta linea es BLOQUEANTE
socket_cliente, addr = servidor.accept()
print(f"IP_Cliente = {addr[0]} Puerto_Cliente = {addr[1]} Protocolo = TCP")
while True:
    datos=socket_cliente.recv(1024) #BLOQUEANTE
    print(f"Cliente: {datos.decode('utf-8')}")
    print(datos.decode('utf-8'))
    a=input("Servidor: ")
    socket_cliente.sendall(a.encode('utf-8'))
socket_cliente.close()