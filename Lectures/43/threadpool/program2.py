import concurrent.futures

def work1():
    print('work1')

def work2():
    print('work2')

pool = concurrent.futures.ThreadPoolExecutor(2)
pool.submit(work1)
pool.submit(work2)

pool.shutdown(wait=True)

print('Main Thread')