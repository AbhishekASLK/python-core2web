class Demo(Exception):
    pass

try:
    x = int(input())
    if(x==0):
        raise Demo
except ValueError:
    print('except Demo')

'''
1. 
class Demo:
    pass

try:
    x = int(input())
    if(x==0):
        raise
except ValueError:
    print('except Demo')

0
Traceback (most recent call last):
  File "/home/abhishekaslk/Desktop/38/userDefinedException.py", line 7, in <module>
    raise
RuntimeError: No active exception to reraise

2.
class Demo:
    pass

try:
    x = int(input())
    if(x==0):
        raise Demo
except ValueError:
    print('except Demo')

0
Traceback (most recent call last):
  File "/home/abhishekaslk/Desktop/38/userDefinedException.py", line 7, in <module>
    raise Demo
TypeError: exceptions must derive from BaseException

3. 
class Demo(Exception):
    pass

try:
    x = int(input())
    if(x==0):
        raise Demo
except ValueError:
    print('except Demo')

Traceback (most recent call last):
  File "/home/abhishekaslk/Desktop/38/userDefinedException.py", line 7, in <module>
    raise Demo
Demo

'''
