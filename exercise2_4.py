import numpy as np
import argparse
#print time in yrs it takes for spaceship to reach destination

def calc_t(distance, speed):
    #time observed from earth
    t_earth = distance / speed

    #time observed from spaceship
    gamma = 1 / np.sqrt(1 - speed**2)
    t_ship = t_earth / gamma

    return t_ship, t_earth
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('distance', type=float, help='the distance to the destination in light years')
    parser.add_argument('speed', type=float, help='the speed of the spaceship as a fraction of the speed of light')

    args = parser.parse_args()

    t_ship, t_earth = calc_t(args.distance, args.speed)

    print(f"The time observed from the spaceship is {t_ship:.2f} years")
    print(f"The time observed from earth is {t_earth:.2f} years")

if __name__ == '__main__':
    main()


    