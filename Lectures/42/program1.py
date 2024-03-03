import threading

class MyThread(threading.Thread):
    
    def __init__(self,x,y):
        super().__init__()
        print(threading.currentThread().getName())
        self.x = x
        self.y = y

    def run(self):
        print("In run method")
        print(threading.current_thread().name)

    
obj = MyThread(10,20)
obj.start()

