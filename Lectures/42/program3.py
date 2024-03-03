import threading

def fun(x,y):
    print(x,y)
    print("In fun")
    print(threading.current_thread().name)

def mun():
    print("In mun")
    print(threading.current_thread().name)

print(threading.current_thread().name)

t1 = threading.Thread(target=fun,args=10)
t2 = threading.Thread(target=mun)

t1.start()
t2.start()
