import numpy as np

arr = np.array([1, 2, 3], dtype=np.int32)
print("Data type:", arr.dtype)

arr = arr.astype(np.float64)
print("Updated type:", arr.dtype)