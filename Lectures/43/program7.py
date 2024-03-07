# Multithreading with Object Oriented Programming

import threading

class MyThread(threading.Thread):
    def run(self):
        print('in run')
        print(threading.current_thread().name)


print('start code')
t1 = MyThread()
t1.start()
