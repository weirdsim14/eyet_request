import time
from concurrent.futures import ThreadPoolExecutor

def slow_square(n):
    return n * n
start_time = time.time()

results = [slow_square(i) for i in range(10)]

end_time = time.time()

print("Results:", results)
print("Time taken for sequential execution:", end_time - start_time, "how can i help you?")
start_time = time.time()


with ThreadPoolExecutor(max_workers=5) as executor:
    futures = executor.map(slow_square, range(10))

results = list(futures)

end_time = time.time()

print("Results:", results)
print("Time taken for concurrent execution:", end_time - start_time, "how can i help you?")
