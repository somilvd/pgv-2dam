import socket

# IPv4 + TCP
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) > UDP
# Interfaz del puerto
servidor.bind(("0.0.0.0", 4444))
# Apertura del puerto
servidor.listen()
# Y ahora viene TCP
while True:
    socket_cliente, addr = servidor.accept() # Esta linea es BLOQUEANTE
    print(f"IP_Cliente = {addr[0]} Puerto_Cliente = {addr[1]} Protocolo = TCP")
    fichero=open(f"archivo_{addr[0]}", "wb")
    while True:
        datos=socket_cliente.recv(1024) #BLOQUEANTE
        if not datos:
            break
        #fichero.write(datos)
        print(f"{addr}: {datos.decode('utf-8')}")
        a=input("Respuesta")
        socket_cliente.sendall(a.encode('utf-8'))
    #fichero.close()
    socket_cliente.close()
servidor.close()