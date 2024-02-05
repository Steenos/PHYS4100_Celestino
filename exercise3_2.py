import numpy as np
import matplotlib.pyplot as plt
# 1. a)  Make a plot of the deltoid curve
#  x = 2 cos θ + cos 2θ, y = 2 sin θ − sin 2θ, where 0 ≤ θ < 2π
theta = np.linspace(0, 2*np.pi, 1000)

x = 2*np.cos(theta) + np.cos(2*theta)
y = 2*np.sin(theta) - np.sin(2*theta)

plt.title("Deltoid curve")
plt.plot(x, y, label='x = 2 cos θ + cos 2θ, y = 2 sin θ - sin 2θ')
plt.legend()
plt.show()

# 2. b) make a plot of the Galilean spiral, r=θ2 for 0 ≤ θ ≤ 10π.
theta = np.linspace(0, 10*np.pi, 1000)
r = theta**2

x = r*np.cos(theta)
y = r*np.sin(theta)

plt.title("Galilean spiral")
plt.plot(x, y, label='r=θ^2')
plt.legend()
plt.show()

# 3. c)  Using the same method, make a polar plot of “Fey’s function”
theta = np.linspace(0, 24*np.pi, 1000)
r = np.exp(np.cos(theta)) - 2 * np.cos(4*theta) + np.sin(theta/12)**5
x = r*np.cos(theta)
y = r*np.sin(theta)
plt.title("Fey's function")

plt.plot(x,y, label="r = exp(cos(θ)) - 2cos(4θ) + sin(θ/12)^5")
plt.legend()
plt.show()


