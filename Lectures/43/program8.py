# Multithreading with Object Oriented Programming

import threading

class MyThread(threading.Thread):

    def __init__(self,x,y):
        
        self.x = x
        self.y = y

    def run(self):
        print('in run')
        print(threading.current_thread().name)

    def add(self):
        print(f'The sum is {self.x+self.y}')

print('start code')
t1 = MyThread(10,20)
t1.start()


'''
OUTPUT:
start code
Traceback (most recent call last):
  File "/home/abhishekaslk/Desktop/Python/Lectures/43/program8.py", line 21, in <module>
    t1.start()
  File "/usr/lib/python3.11/threading.py", line 956, in start
    raise RuntimeError("thread.__init__() not called")
RuntimeError: thread.__init__() not called

'''
