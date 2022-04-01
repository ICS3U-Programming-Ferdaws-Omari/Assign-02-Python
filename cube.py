#!/usr/bin/env python3
# Created by: Ferdaws
# Created in: March. 08, 2022
# This program asks the user for a side
# of the cube in mm. It then
# calculates and displays the area and
# vloume.
import math


def main():
    # Ask the user for one of the sides of the cube and the unit
    print("Today we will calculate the area and")
    print("volume of a cube")
    side = float(input("Enter the length of one of the sides : "))
    units = input("Enter the units: ")

    # Calculate area and volume of the cube
    area = 6 * side ** 2
    volume = side ** 3

    # display the results to the user and round it to two decimal places
    print("")
    print("Area = {:.2f} {}". format(area, units))
    print("Volume = {:.2f} {}". format(volume, units))


if __name__ == "__main__":
    main()
