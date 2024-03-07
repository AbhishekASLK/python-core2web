import concurrent.futures

def work1():
    print('work1')

def work2():
    print('work2')

tp = concurrent.futures.ThreadPoolExecutor()
print(tp._max_workers)

'''
ThreadPoolExecutor is often used to:

- CPU bound task which releases GIL
- I/O bound task (which releases GIL, of course)

We use cpu_count + 4 for both types of tasks.
But we limit it to 32 to avoid consuming surprisingly large resource
on many core machine.
'''