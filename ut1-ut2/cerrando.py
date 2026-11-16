import threading

dato = 0
hilos = []
lock = threading.Lock()

def suma():
    global dato, lock

    print(f"dato = {dato} modificado por {threading.current_thread().name}")
    lock.acquire()
    a = dato
    a += 1
    dato = a
    lock.release()

for i in range(3):
    t = threading.Thread(target = suma)
    t.start()
    hilos.append(t)

for i in hilos:
    i.join()
print(f"El MT imprime {dato}")