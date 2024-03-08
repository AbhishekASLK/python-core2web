import concurrent.futures

pool = concurrent.futures.ThreadPoolExecutor(max_workers=5)
print(pool._threads)

