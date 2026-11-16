import os, time

print("Esto solo lo ejecuta el padre")

pid=os.fork()

for i in range(10):

    if pid == 0:
        print(f"Hijo: {os.getpid()}.Iteración {i}")
    else:
        print(f"Padre: {os.getpid()}.Iteración {i}")
