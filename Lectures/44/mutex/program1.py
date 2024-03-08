import threading

# Mutex (using Lock)
mutex = threading.Lock()

# Shared variable
counter = 0

# Function to increment counter using Mutex
def increment_with_mutex():
    global counter
    for _ in range(10000):
        with mutex:
            counter += 1

# Creating threads for Mutex
mutex_threads = []
for _ in range(5):
    t = threading.Thread(target=increment_with_mutex)
    mutex_threads.append(t)
    t.start()

for t in mutex_threads:
    t.join()

print("Counter with Mutex:", counter)  # Expected value: 50000
