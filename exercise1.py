import math
import sys

if __name__ == '__main__':
    g=9.81
    #height is the first argument in sys.argv
    h = float(sys.argv[1])
    #calculate time it takes to fall
    t=math.sqrt(2*h/g)

    print(f"The time it takes to fall is: {t:.2f} seconds")







	