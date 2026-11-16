import threading

realizado = False;

def trabajo():
    global realizado
    if not realizado:
        realizado=True
        print(f"Lo hice yo {threading.current_thread().name}")
    else:
        print(f"Yo no pude que soy {threading.current_thread().name}")

t=threading.Thread(target=trabajo)
t.start()
trabajo()