import numpy as np
import matplotlib.pyplot as plt
import math
x = np.linspace(-2, 2, 100)

def func(x): 
    return 0.5 * np.tanh(2 * x)

def derive(func, x, h=1e-5):
    return (func(x + h/2) - func(x - h/2)) / h

#print(derive(func, x))


plt.plot(x, derive(func, x), label='Derivative of 0.5*tanh(2x)')
#plt.plot(x, 1/(np.cos(2*x)**2), label='Analytical derivative')
plt.legend()
plt.show()





