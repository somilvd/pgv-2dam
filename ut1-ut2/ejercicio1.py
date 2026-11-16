import os

print("Esto solo lo ejecuta el padre")

pid=os.fork()

if pid == 0:
    print(f"Soy el hijo y mi PID es: {os.getpid()}")
    print(f"El PID de mi padre es: {os.getppid()}")
else:
    print(f"Soy el padre y mi PID es: {os.getpid()}")
    print(f"El PID de mi padre es: {os.getppid()}")
    