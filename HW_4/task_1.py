"""Напишите программу на Python, которая будет находить сумму элементов массива из 1000000 целых чисел.
Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
Массив должен быть заполнен случайными целыми числами от 1 до 100.
При решении задачи нужно использовать многопоточность, многопроцессорность и асинхронность.
В каждом решении нужно вывести время выполнения вычислений."""

import threading
import multiprocessing
import asyncio
import random
import time


def sum_array(arr, start, end, result):
    partial_sum = sum(arr[start:end])
    result.put(partial_sum)


async def sum_array_async(arr, start, end, result):
    partial_sum = sum(arr[start:end])
    result.put(partial_sum)


async def main():
    arr = [random.randint(1, 100) for _ in range(1000000)]

    start_time_async = time.time()
    result_async = multiprocessing.Queue()
    tasks_async = []
    num_tasks_async = 4
    chunk_size_async = len(arr) // num_tasks_async
    for i in range(num_tasks_async):
        start_async = i * chunk_size_async
        end_async = start_async + chunk_size_async if i < num_tasks_async - 1 else len(arr)
        task_async = sum_array_async(arr, start_async, end_async, result_async)
        tasks_async.append(task_async)
    total_sum_async = 0
    await asyncio.gather(*tasks_async)
    while not result_async.empty():
        total_sum_async += result_async.get()
    end_time_async = time.time()
    print("Сумма элементов массива (асинхронность):", total_sum_async)
    print("Время выполнения (асинхронность):", end_time_async - start_time_async, "секунд")


if __name__ == '__main__':
    arr = [random.randint(1, 100) for _ in range(1000000)]

    start_time_thread = time.time()
    # Многопоточный подход
    result_thread = multiprocessing.Queue()  # Changed here
    num_threads_thread = 4
    threads_thread = []
    chunk_size_thread = len(arr) // num_threads_thread
    for i in range(num_threads_thread):
        start_thread = i * chunk_size_thread
        end_thread = start_thread + chunk_size_thread if i < num_threads_thread - 1 else len(arr)
        thread = threading.Thread(target=sum_array, args=(arr, start_thread, end_thread, result_thread))
        thread.start()
        threads_thread.append(thread)
    for thread in threads_thread:
        thread.join()
    total_sum_thread = 0
    while not result_thread.empty():
        total_sum_thread += result_thread.get()  # Changed here
    end_time_thread = time.time()
    print("Сумма элементов массива (многопоточность):", total_sum_thread)
    print("Время выполнения (многопоточность):", end_time_thread - start_time_thread, "секунд")

    start_time_process = time.time()
    # Многопроцессорный подход
    result_process = multiprocessing.Queue()
    num_processes_process = 4
    processes_process = []
    chunk_size_process = len(arr) // num_processes_process
    for i in range(num_processes_process):
        start_process = i * chunk_size_process
        end_process = start_process + chunk_size_process if i < num_processes_process - 1 else len(arr)
        process = multiprocessing.Process(target=sum_array, args=(arr, start_process, end_process, result_process))
        process.start()
        processes_process.append(process)
    for process in processes_process:
        process.join()
    total_sum_process = 0
    while not result_process.empty():
        total_sum_process += result_process.get()
    end_time_process = time.time()
    print("Сумма элементов массива (многопроцессорность):", total_sum_process)
    print("Время выполнения (многопроцессорность):", end_time_process - start_time_process, "секунд")

    asyncio.run(main())
