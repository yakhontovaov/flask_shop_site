import multiprocessing
import random
import time

arr = [random.randint(1, 100) for _ in range(1000000)]


def sum_array(arr, start, end, result):
    partial_sum = sum(arr[start:end])
    result.put(partial_sum)


if __name__ == '__main__':
    start_time = time.time()
    result = multiprocessing.Queue()

    num_processes = 4
    processes = []
    chunk_size = len(arr) // num_processes
    for i in range(num_processes):
        start = i * chunk_size
        end = start + chunk_size if i < num_processes - 1 else len(arr)
        process = multiprocessing.Process(target=sum_array, args=(arr, start, end, result))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

    total_sum = 0
    while not result.empty():
        total_sum += result.get()

    end_time = time.time()
    print(f'Сумма элементов массива (многопроцессорность):, {total_sum}')
    print(f'Время выполнения (многопроцессорность): {end_time - start_time} секунд')
