import numpy as np
import astropy.constants as c
import astropy.units as u
#import scipy.constants as cons 
#print(f"The values of G and h aee {cons.G} and {cons.h}")
# {cons.value('electron g factor')}

#print(f"Two electrons have a mass of {2*c.m_e}")
#print(f"That is {2*c.m_e*u.g/u.kg} in  grams")

constants = c.k_B ** 4  / (4 * np.pi * c.h**3 * c.c**2)

def my_function(z):
    return ((1 / z - 1)**2) * ((z / (z - 1))**3 / (np.exp(z / (z - 1)) - 1))

N = 10
a = 0.0
b = 1.0
h = (b-a)/N
s = 0.5*my_function(a) + 0.5*my_function(b)
for k in range(1,N):
    s += f(a+k*h)
    print(h*s)





