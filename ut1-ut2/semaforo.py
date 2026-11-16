import threading, subprocess, time, random

semaforo = threading.Semaphore(2)
def ping():
    global semaforo
    semaforo.acquire()
    print(threading.current_thread().name, flush = True)
    subprocess.run(["ping", "-c", "1", "8.8.8.8"])
    time.sleep(1)
    semaforo.release()

for i in range(10):
    t = threading.Thread(target = ping)
    t.start()