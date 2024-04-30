import numpy as np
import matplotlib.pyplot as plt

V = 20
w = 1
m_e = 9.1094e-31
h = 1.0545718e-34 
w = 1e-9


eV_to_J = 1.60218e-19  
E = np.linspace(0, V, 1000) * eV_to_J
V_joules = V * eV_to_J

'''
1)
For an electron (mass 9.1094×10−31 kg) in a well with V = 20eV 
and w = 1nm, write a Python program to plot the three quantities
'''
y1 = np.tan(np.sqrt(w**2 * m_e * E / (2 * h**2)))
y2 = np.sqrt((V_joules - E) / E, where=E!=0)
y3 = -np.sqrt(E / (V_joules - E), where=(V_joules-E)!=0)

y1[:-1][np.diff(y1) < 0] = np.NaN #removes lines to infinity
#bound inifinity
y1 = np.clip(y1, -20, 20)

plt.figure(figsize=(10, 6))
#plotting y1
plt.plot(E / eV_to_J, y1)
plt.plot(E / eV_to_J, y2)
plt.plot(E / eV_to_J, y3)
plt.ylim(-4,4)
plt.xlim(0,20)
plt.show()



