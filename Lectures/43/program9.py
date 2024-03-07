# Multithreading with Object Oriented Programming 
# without inheritance with Thread class

import threading

class MyThread():

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def add(self):
        print(self.x)
        print(self.y)
        print(f'The sum is {self.x+self.y}')
        print(threading.current_thread().name)

print('start code')
obj = MyThread(10,20)
t1 = threading.Thread(target=obj.add)
t1.start()


