import threading

print(threading.active_count())

'''
OUTPUT:
1

active_count() returns the length of the list provided by the enumerate function which 
returns the list of thread objects which are currently alive
'''