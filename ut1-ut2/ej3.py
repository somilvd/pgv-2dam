import os,time, sys

pid=os.fork()

if pid == 0:
    print(f"Hijo PID: {os.getpid()}")
    input("Ingrese su nombre:")
    time.sleep(5)
    print("El proceso hijo va a terminar")
    sys.exit(5)
else: 
    pid, status = os.wait()
    status = os.waitstatus_to_exitcode(status)
    print(f"PID de mi Hijo: {pid} y estado {status}")
    print(f"PID Padre: {os.getpid()}")

