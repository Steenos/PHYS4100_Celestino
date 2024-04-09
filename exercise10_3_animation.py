import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random

# Define the lattice size
L = 101

# define total steps
total_steps = 1000000

# initialize in the center
position = np.array([L//2, L//2])

# Define the possible movements: up, down, left, right
movements = np.array([[0, 1], [0, -1], [-1, 0], [1, 0]])

# Store the path
path = [position.copy()]

# Perform random walk
for _ in range(total_steps):
    # Choose a random direction
    move = random.choice(movements)
    new_position = position + move
    
    # Check if the new position is within the lattice bounds
    if 0 <= new_position[0] < L and 0 <= new_position[1] < L:
        position = new_position
        path.append(position.copy())


# Convert path to an array for easier handling
path = np.array(path)
print(f"total steps done: {len(path)}") 
# Animation
fig, ax = plt.subplots()


ax.set_xlim(0, L-1)
ax.set_ylim(0, L-1)
ax.set_aspect('equal')

line, = ax.plot([], [], lw=2)

# Initialize the line
def init():
    line.set_data([], [])
    return (line,)

# Animation update function
def update(frame):
    line.set_data(path[:frame, 0], path[:frame, 1])
    return (line,)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=len(path), init_func=init, blit=True, interval=10)

plt.show()
