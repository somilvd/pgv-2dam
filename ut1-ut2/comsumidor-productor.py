import threading, queue, time

q = queue.Queue(10)
semaforo = threading.Semaphore(10)
evento = threading.Event()

def productor():
    global q, semaforo
    while True:
        semaforo.acquire()
        q.put(threading.current_thread().name)
        evento.set()

def consumidor():
    global q, semaforo
    while True:
        evento.wait()
        print(q.get())
        semaforo.release()
        time.sleep(1)
        evento.clear()



for i in range(2):
    t = threading.Thread(target=productor)
    t.start()

for i in range(1):
    t = threading.Thread(target=consumidor)
    t.start()