import time
import numpy as np


ROWS   = 500
COLS   = 500
REPEAT = 10

total_vector = [[i + j for j in range(COLS)] for i in range(ROWS)]
np_vector    = np.array(total_vector)


# Vector Operations from SCRATCH:

def add_vector(total_vector):
    result = []
    for i in range(max(len(v) for v in total_vector)):
        vector_sum = 0
        for j in range(len(total_vector)):
            if i < len(total_vector[j]):
                vector_sum += total_vector[j][i]
        result.append(vector_sum)
    return result

def sub_vector(total_vector):
    result = total_vector[0][:]
    for vector in total_vector[1:]:
        for i in range(len(vector)):
            result[i] -= vector[i]
    return result

def sum_vector(lst):
    result = 0
    for v in lst:
        result += v
    return result

def dot_vector_product(total_vector):
    result = []
    for i in range(len(total_vector[0])):
        mul = 1
        for j in range(len(total_vector)):
            mul *= total_vector[j][i]
        result.append(mul)
    return sum_vector(result)


# Using Numpy


def numpy_add(v): return np.sum(v, axis=0)

def numpy_sub(v):
    r = v[0].copy()
    for row in v[1:]:
        r -= row
    return r

def numpy_dot(v): return np.sum(np.prod(v, axis=0))






# TIMER FUNCTION

def benchmark(func, *args, repeat=REPEAT):
    times = []
    for _ in range(repeat):
        start = time.perf_counter()
        func(*args)
        end   = time.perf_counter()
        times.append(end - start)
    return min(times)


ops = [
    ("ADD", add_vector,        numpy_add, total_vector, np_vector),
    ("SUB", sub_vector,        numpy_sub, total_vector, np_vector),
    ("DOT", dot_vector_product, numpy_dot, total_vector, np_vector),
]

COL = 14
print(f"\n{'='*55}")
print(f"  BENCHMARK  —  {ROWS}×{COLS} vectors  |  best of {REPEAT} runs")
print(f"{'='*55}")
print(f"{'Op':<6} {'Pure Python':>{COL}} {'NumPy':>{COL}} {'Speedup':>{COL}}")
print(f"{'-'*55}")

for name, py_fn, np_fn, py_data, np_data in ops:
    t_py = benchmark(py_fn, py_data)
    t_np = benchmark(np_fn, np_data)
    print(f"{name:<6} {t_py:>{COL}.6f}s {t_np:>{COL}.6f}s {t_py/t_np:>{COL}.1f}x")

print(f"{'='*55}")
