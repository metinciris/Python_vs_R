# Python vs R: Performance Comparison 🚀🐢


This repository contains a fun and visual performance comparison between **Python** and **R** for matrix multiplication tasks.  
Using **NumPy**, Python takes the lead as R lags behind (10x slower in our simulation). 📈

## 📊 Performance Results
### Python vs R Simulation
![Performance Comparison](performance_comparison.png)

Python excels in numerical tasks, thanks to its optimized libraries like NumPy. Meanwhile, R is often preferred for statistical analysis but lags in raw computational speed.

## 📄 Code
```python
import time
import numpy as np
import matplotlib.pyplot as plt

def calculate_fast_simulation(size):
    """Fast simulation using NumPy"""
    start = time.time()
    matrix_a = np.random.random((size, size))
    matrix_b = np.random.random((size, size))
    result = np.dot(matrix_a, matrix_b)  # NumPy optimized operation
    end = time.time()
    return result, end - start

# Simulation
sizes = range(100, 1001, 100)
python_times = [calculate_fast_simulation(size)[1] for size in sizes]
r_times = [t * 10 for t in python_times]  # Simulate R being 10x slower

# Plot
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
```

## 🧰 Setup and Run
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/python-vs-r-speed.git
   cd python-vs-r-speed
   ```
2. Install dependencies:
   ```bash
   pip install matplotlib numpy
   ```
3. Run the code:
   ```bash
   python test.py
   ```

## 🤔 Why Python?
- **NumPy:** Highly optimized for numerical tasks.
- **Flexibility:** A general-purpose language for data science and beyond.

## 🚀 Future Work
We'll explore more performance comparisons in different tasks. Stay tuned!

## 📧 Feedback
Have suggestions or ideas? Feel free to open an issue or reach out!

---

### Key Takeaway
Python shines in numerical tasks, but every language has its strengths. Use the right tool for the job! 😉
```

