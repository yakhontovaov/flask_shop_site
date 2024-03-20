import threading
import random
import time

arr = [random.randint(1, 100) for _ in range(1000000)]


def sum_array(arr, start, end, result):
    partial_sum = sum(arr[start:end])
    result.append(partial_sum)


start_time = time.time()
result = []

num_threads = 4
threads = []
chunk_size = len(arr) // num_threads
for i in range(num_threads):
    start = i * chunk_size
    end = start + chunk_size if i < num_threads - 1 else len(arr)
    thread = threading.Thread(target=sum_array, args=(arr, start, end, result))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

total_sum = sum(result)
end_time = time.time()
print(f'Сумма элементов массива (многопоточность):, {total_sum}')
print(f'Время выполнения (многопоточность): {end_time - start_time} секунд')
