# Multithreading with procedure orientation

import threading

def fun():
    print(threading.current_thread().name)
    for i in range(5):
        print('fun')

def mun():
    print(threading.current_thread().name)
    for i in range(5):
        print('mun')

print(threading.current_thread().name)

t1 = threading.Thread(target=fun)
t2 = threading.Thread(target=mun)

t1.start()
t2.start()
t1.join()
t2.join()
print(t1.is_alive()) # Abhi yaha pe t1 ho ya t2 ho, dono mare hi milenge, because main thread, ruka hi 
print(t2.is_alive()) # tha for dying the t1 and t2 thread

t1.join() # Main thread wait until the t1 ended with his work
t2.join() # Main thread wait until the t2 ended with his work

for i in range(10):
    print('main thread')