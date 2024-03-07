# Multithreading with procedure orientation

import threading

def fun():
    print(threading.current_thread().name)
    for i in range(6):
        print('fun')

def mun():
    print(threading.current_thread().name)
    for i in range(6):
        print('mun')

print(threading.current_thread().name)

t1 = threading.Thread(target=fun)
t2 = threading.Thread(target=mun)

t1.start()
t2.start()