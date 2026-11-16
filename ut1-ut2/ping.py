import subprocess, time, os, sys

ahora=time.time()

for i in range(10):
    pid=os.fork()
    if pid==0:
        subprocess.run(['ping', '-c 2','-i 2' ,'8.8.8.8'])
        sys.exit()

for i in range(10):
    os.wait()
print(time.time()-ahora)
