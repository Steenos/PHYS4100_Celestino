import numpy as np

def f(x, N):
	return x**4 - 2*x + 1
#trapezoid rule
N = 10
a =0.0
b=2.0
h=(b-a)/N
s = 0.5*f(a) + 0.5*f(b)

for k in range(1,N):
	s += f(a + k*h)

print(h*s)

#calculate error 10 steps and 20 steps
error = (1/3) 


#Simpsons Rule
def simpson(a):
    for k in range(1,N):
        s+= 4 * trapezoid(a+k*h)
    for k in range(2,N-1):
        s+= 2* trapezoid(a+k*h)

N = 10  
a = 0.0
b = 2.0
h = (b-a)/N
s = simpson(a) + simpson(b)
print(h*s/3)

"""def simpson():

    for k in range(1,N,2):
        s += 4*simpson(a+k*h)
    for k in range(2,N-1,2):
        s += 2*simpson(a+k*h)
    return s
N = 10  
a = 0.0
b = 2.0
h = (b-a)/N
s = simpson(a) + simpson(b)



print(h*s/3)"""

