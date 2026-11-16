import threading, time

dato = 0

def suma1():
    global dato
    a=dato
    a += 1
    dato = a 

def suma3():
    global dato
    time.sleep(0.001)
    a = dato
    a += 3
    dato = a 

t1 = threading.Thread(target=suma1)
t2 = threading.Thread(target=suma3)
t1.start()
t2.start()
t1.join()
t2.join()
print(f"El valor de dato es {dato}")