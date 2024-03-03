import threading

class MyThread():
    
    def __init__(self,x,y):
        super().__init__()
        print(threading.current_thread().name)
        self.x = x
        self.y = y

    def fun(self):
        print(self.x)
        print(self.y)
        print("In run method")
        print(threading.current_thread().getName())

    
obj = MyThread(10,20)

thread1 = threading.Thread(target=obj.fun)
thread1.start()

