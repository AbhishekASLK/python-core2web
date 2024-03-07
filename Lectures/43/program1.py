import threading

print(threading.enumerate())


'''
Output:
[<_MainThread(MainThread, started 140345325400128)>]

This is not an method (Global API functions), this is an function written in threading.py
Returns the list of threads which are currently alive

'''