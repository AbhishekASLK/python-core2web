import threading

print('Start Code')

def fun():
    print('in fun')

# print(threading.currentThread())
print(threading.current_thread().name)

fun()
