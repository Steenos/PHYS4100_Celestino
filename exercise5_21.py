import numpy as np
import matplotlib.pyplot as plt


# F/m Vacuum electric permittivity
epsilon_0 = 8.85e-12  # Vacuum permittivity in F/m
grid_size = 101  # Grid dimensions


def electric_potential(q,x1,y1,x2,y2):
    r = np.sqrt((x2-x1)**2 + (y2-y1)**2)
    #r[r == 0] = 1e-12  # Avoid division by zero
    return q / (4 * np.pi * epsilon_0 * r)





#charge 1
#arr[50,45] = -1

#charge 2
#arr[50,55] = 1

#chare 1 location
charge_1_x = 50
charge_1_y = 45

#charge 2 location
charge_2_x = 50
charge_2_y = 55

potentials = np.zeros((grid_size, grid_size))

for i in range(101):
    x = i 
    for j in range(101):
        y=j
        potentials[i, j] = electric_potential(-1, charge_1_x, charge_1_y, x, y) + \
                           electric_potential(1, charge_2_x, charge_2_y, x, y)
        
        

X = np.arange(0,101)
Y = np.arange(0,101)
# Plotting the potential
plt.figure(figsize=(10, 8))
plt.contourf(X, Y, potentials, levels=50, cmap='viridis')
plt.colorbar(label='Potential (V)')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title('Electric Potential')
plt.show()

#electric field is -gradient * potential

# Calculate the gradient (partial derivatives) of the potential
dPhi_dx, dPhi_dy = np.gradient(potentials, 1, 1)

print(dPhi_dx.shape)

E_x = - dPhi_dx
E_y = - dPhi_dy


U, V = E_x, E_y 

fig, ax = plt.subplots()
q = ax.quiver(X, Y, U , V ,
               scale=7e10, pivot='mid')
#ax.quiverkey(q, X=0.9, Y=0.9, U=2,
             #label='Quiver key, length = 10', labelpos='E')

plt.xlabel('x (cm)')
plt.ylabel('y (cm)')
plt.title('Electric Field Vectors')
plt.xlim(40,60)
plt.ylim(40,60)
#plt.set_ylmin()

plt.show()


