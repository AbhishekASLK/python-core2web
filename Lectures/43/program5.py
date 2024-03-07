import os
import threading

for i in range(1,11):
    print(i,end=' ')
print()

print(os.getpid())
print(threading.current_thread().name)