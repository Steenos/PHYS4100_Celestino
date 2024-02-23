import numpy as np
import matplotlib.pyplot as plt
import time
N=999999
k=1
h=2/N
I=0
start = time.time()
for k in range(1,N+1):
    x_k = -1 + h*k
    y_k = np.sqrt(1-x_k**2)
    I = I + y_k*h
end = time.time()
print(f"Program took: {end-start} seconds to run")
print(f"Integral is: {I}")
    