import time
import numpy as np
import matplotlib.pyplot as plt

# Problem size
N = 10_000_000

# Data structures
# Poor locality (Python objects)
data_list = list(range(N))    
# Good locality (contiguous memory)                 
data_array = np.arange(N, dtype=np.int64)         

# Functions
def sum_of_squares_list(data):
    """Naive Python loop with poor data locality."""
    total = 0
    for x in data:
        total += x * x
    return total

def sum_of_squares_numpy(data):
    """Locality-optimized NumPy version with vectorization."""
    return np.sum(data * data)

# Benchmarking
# Python list version
start = time.time()
result_list = sum_of_squares_list(data_list)
time_list = time.time() - start

# NumPy array version
start = time.time()
result_numpy = sum_of_squares_numpy(data_array)
time_numpy = time.time() - start

# Print results
print(f"Python list time: {time_list:.4f} s")
print(f"NumPy array time: {time_numpy:.4f} s")
print(f"Speedup: {time_list / time_numpy:.2f}x")

# Chart Generation
labels = ['Python List', 'NumPy Array']
times = [time_list, time_numpy]

plt.figure(figsize=(8, 5))
plt.bar(labels, times, color=['#d95f02', '#1b9e77'])
plt.ylabel("Execution Time (seconds)")
plt.title("Performance Comparison: Python List vs NumPy (Data Locality Optimization)")
plt.tight_layout()
plt.show()
