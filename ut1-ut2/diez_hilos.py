import threading

def hilo():
    print(f"{threading.current_thread().name}")

def entrada():
    dato=input("Dame el dato: ")

hilos=[]
t=threading.Thread(target=entrada)

t.start()
print(f"{threading.current_thread().name}")
for i in range(10):
    t=threading.Thread(target=hilo)
    hilos.append(t)

for i in hilos:
    i.start()