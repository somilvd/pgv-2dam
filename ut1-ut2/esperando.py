import threading

def hilo_secundario():
    for i in range(1000):
        print("Y", end="", flush=True)

t=threading.Thread(target=hilo_secundario, daemon=True)
t.start()
for i in range(10):
    print("X", end="", flush=True)
t.join()
print("EL hilo secundario ya terminó. ADIOS")


