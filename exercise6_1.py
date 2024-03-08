import numpy as np

A = np.array([[4,-1,-1,-1],
                     [-1,3,0,-1],
                     [-1,0,3,-1],
                     [-1,1,-1,4]], float)

v = np.array([-4,3,9,7], float)
N = len(v)
# Gaussian Elimination
for m in range(N):
    #divide by the diagonal element
    div = A[m,m]
    A[m,:] /= div
    v[m] /= div

    #subtract from the lower rows
    for i in range(m+1,N):
        mult = A[i,m]
        A[i,:] -= mult*A[m,:]
        v[i] -= mult*v[m]
    
    #Backsubstitution
    x = np.empty(N, float)
    for m in range(N-1,-1,-1):
        x[m] = v[m]
        for i in range(m+1,N):
            x[m] -= A[m,i]*x[i]

print(x)
print(np.linalg.solve(A,v))