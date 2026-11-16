import threading, subprocess

evento = threading.Event()

def ping():
    global evento
    evento.wait()
    subprocess.run(["ping", "-c", "1", "8.8.8.8"])

for i in range(10):
    t = threading.Thread(target = ping)
    t.start()

letra = ""
while letra != "m":
    letra = input("Dame una m ")
evento.set()
    