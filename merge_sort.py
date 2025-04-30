import random
import os
import time
import matplotlib.pyplot as plt

def merge_sort(arr):
    iterations = 0
    
    if len(arr) <= 1:
        return arr, iterations
    
    mid = len(arr) // 2
    left, left_iter = merge_sort(arr[:mid])
    right, right_iter = merge_sort(arr[mid:])
    
    iterations = left_iter + right_iter
    
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        iterations += 1 
            
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    iterations += len(left[i:]) + len(right[j:]) 
    
    merged.extend(left[i:])
    merged.extend(right[j:])
    
    return merged, iterations

def generate_data():
    if not os.path.exists('datasets'):
        os.makedirs('datasets')

    sizes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000,
             1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000,
             6000, 7000, 8000, 9000, 10000]
    
    for size in sizes:
        data = [random.randint(0, 10000) for _ in range(size)]

        with open(f'datasets/data_{size}.txt', 'w') as f:
            f.write(','.join(map(str, data)))

def load_dataset(size):
    with open(f'datasets/data_{size}.txt', 'r') as f:
        return list(map(int, f.read().split(',')))
    
def measure_time():
    sizes = []
    times = []
    iterations = []

    files = os.listdir('datasets')
    sizes = sorted([int(f.split('_')[1].split('.')[0]) for f in files])

    for size in sizes:
        data = load_dataset(size)

        start_time = time.perf_counter()
        sorted_data, iter_count = merge_sort(data.copy())
        end_time = time.perf_counter()

        average_time = (end_time - start_time)

        times.append(average_time)
        iterations.append(iter_count)

        print(f"Размер: {size}, Время: {average_time:.2f} с, Итерации: {iter_count}")

    return sizes, times, iterations

def draw_plot(sizes, times, iterations):

    plt.figure(figsize=(14, 6))
    
    plt.subplot(1, 2, 1)
    plt.plot(sizes, times, 
         color='blue',
         linestyle='-',
         marker='o',
         markersize=5)
    plt.xlabel('Размер массива')
    plt.ylabel('Время (мс)')
    plt.title('Время выполнения Merge Sort')
    plt.grid(True)
    
    plt.subplot(1, 2, 2)
    plt.plot(sizes, iterations, 
         color='red',
         linestyle='-',
         marker='o',
         markersize=5)
    plt.xlabel('Размер массива')
    plt.ylabel('Количество итераций')
    plt.title('Сложность Merge Sort')
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()

def main():
    if not os.path.exists('datasets'):
        generate_data()

    sizes, times, iterations = measure_time()

    draw_plot(sizes, times, iterations)

if __name__ == '__main__':
    main()

