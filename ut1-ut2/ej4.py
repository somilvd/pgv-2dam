import os

pid=os.fork()

a = 5 + pid

print(a)
