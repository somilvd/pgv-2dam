import threading, time

def Saludando():
    time.sleep(1)
    print("Soy el hilo secundario")

print("Soy el Main Thread")
t=threading.Thread(target=Saludando)
t.start()
print("Soy el Main Thread después")
