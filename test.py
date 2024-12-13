import time
import numpy as np
import matplotlib.pyplot as plt

# Hızlı işlem için NumPy kullanımı
# R'nin yavaş olacağı bir simülasyon örneği

def calculate_fast_simulation(size):
    """Fast simulation using NumPy"""
    start = time.time()
    matrix_a = np.random.random((size, size))
    matrix_b = np.random.random((size, size))
    result = np.dot(matrix_a, matrix_b)  # NumPy hızlandırılmış işlem
    end = time.time()
    return result, end - start

# Hızlı işlem
size = 1000
print("Simülasyon boyutu: ", size)
fast_result, fast_time = calculate_fast_simulation(size)
print(f"Python ile işlem süresi: {fast_time:.5f} saniye")

# Görselleştirme için Python ve R sürelerini simüle et
python_times = [calculate_fast_simulation(size)[1] for size in range(100, 1001, 100)]
r_times = [t * 10 for t in python_times]  # R'nin yaklaşık 10 kat yavaş olduğunu varsayıyoruz
sizes = range(100, 1001, 100)

# Karşılaştırma grafiği
plt.figure(figsize=(10, 6))
plt.plot(sizes, python_times, label='Python', marker='o')
plt.plot(sizes, r_times, label='R', marker='o')
plt.title('Python vs R Performance Comparison')
plt.xlabel('Matrix Size (N x N)')
plt.ylabel('Time (seconds)')
plt.legend()
plt.grid(True)
plt.savefig("performance_comparison.png", dpi=300)
plt.show()
