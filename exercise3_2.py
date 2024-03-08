import numpy as np
import matplotlib.pyplot as plt
import argparse

def deltoid():
    theta = np.linspace(0, 2*np.pi, 1000)

    x = 2*np.cos(theta) + np.cos(2*theta)
    y = 2*np.sin(theta) - np.sin(2*theta)

    return x,y,theta
def galilean_spiral():
    theta = np.linspace(0, 10*np.pi, 1000)
    r = theta**2

    x = r*np.cos(theta)
    y = r*np.sin(theta)

    return x,y,r,theta

def feys_function():
    theta = np.linspace(0, 24*np.pi, 1000)
    r = np.exp(np.cos(theta)) - 2 * np.cos(4*theta) + np.sin(theta/12)**5
    x = r*np.cos(theta)
    y = r*np.sin(theta)
    
    return x,y,r,theta

parser = argparse.ArgumentParser(
                    prog='Visualize curves',
                    description='Visualize the deltoid, galilean spiral and feys function',
                    )
parser.add_argument('-sp', '--subplots', help='Make subplots of the three functions',
                    action='store_true') 

parser.add_argument('-graph_type', choices=['deltoid', 'galilean', 'feys'], help='Choose which graph to plot')

args = parser.parse_args()

def main():
    # if args.subplots is True, make subplots of the three functions
    if args.subplots:
        fig, ax = plt.subplots(3, 1, figsize=(10, 10))
        x1, y1, theta1 = deltoid()
        x2,y2,r2,theta2 = galilean_spiral()
        x3,y3,r3,theta3 = feys_function()
    
        ax[0].plot(x1, y1, label='x = 2 cos θ + cos 2θ, y = 2 sin θ - sin 2θ')
        ax[0].set_title("Deltoid curve")
        ax[0].legend()

        ax[1].plot(x2, y2, label='r=θ^2')
        ax[1].set_title("Galilean spiral")
        ax[1].legend()

        ax[2].plot(x3,y3, label="r = exp(cos(θ)) - 2cos(4θ) + sin(θ/12)^5")
        ax[2].set_title("Fey's function")
        ax[2].legend()

        plt.show()
    # if args.graph_type is given, plot the chosen graph
    elif args.graph_type == 'deltoid':
        x1, y1, theta1 = deltoid()
        plt.plot(x1, y1, label='x = 2 cos θ + cos 2θ, y = 2 sin θ - sin 2θ')
        plt.legend()
        plt.show()
    elif args.graph_type == 'galilean':
        x2,y2,r2,theta2 = galilean_spiral()
        plt.plot(x2, y2, label='r=θ^2')
        plt.legend()
        plt.show()
    elif args.graph_type == 'feys':
        x3,y3,r3,theta3 = feys_function()
        plt.plot(x3,y3, label="r = exp(cos(θ)) - 2cos(4θ) + sin(θ/12)^5")
        plt.legend()
        plt.show()
    # if no arguments are given, plot all three graphs
    else:
        x1, y1, theta1 = deltoid()
        x2,y2,r2,theta2 = galilean_spiral()
        x3,y3,r3,theta3 = feys_function()
        plt.plot(x1, y1, label='x = 2 cos θ + cos 2θ, y = 2 sin θ - sin 2θ')
        plt.title("Deltoid curve")
        plt.legend()
        plt.show()
        plt.plot(x2, y2, label='r=θ^2')
        plt.title("Galilean spiral")
        plt.legend()
        plt.show()
        plt.plot(x3,y3, label="r = exp(cos(θ)) - 2cos(4θ) + sin(θ/12)^5")
        plt.title("Fey's function")
        plt.legend()
        plt.show()

if __name__ == '__main__':
    main()
