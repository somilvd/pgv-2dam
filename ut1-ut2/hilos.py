import threading, time

hilos=[]
def otro_hilo():
    for i in range(1000):
        time.sleep(0.001)
        print(f"Y={i}", end="", flush=True)

t=threading.Thread(target=otro_hilo)
t.start()
hilos.append(t)
print(t.name)
for i in range(1000):
    time.sleep(0.001)
    print(f"X={i}", end="", flush=True)
print("\n", end="")
t=threading.Thread(target=otro_hilo, daemon=True)
t.start()
hilos.append(t)
print(t.name)
for hilo in hilos:
    print(hilo.name)
