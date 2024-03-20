import asyncio
import random
import time

arr = [random.randint(1, 100) for _ in range(1000000)]


async def sum_array(arr, start, end):
    partial_sum = sum(arr[start:end])
    return partial_sum


async def main():
    start_time = time.time()

    tasks = []
    num_tasks = 4
    chunk_size = len(arr) // num_tasks
    for i in range(num_tasks):
        start = i * chunk_size
        end = start + chunk_size if i < num_tasks - 1 else len(arr)
        task = sum_array(arr, start, end)
        tasks.append(task)

    total_sum = sum(await asyncio.gather(*tasks))

    end_time = time.time()
    print(f'Сумма элементов массива (асинхронность):, {total_sum}')
    print(f'Время выполнения (асинхронность): {end_time - start_time} секунд')


asyncio.run(main())
