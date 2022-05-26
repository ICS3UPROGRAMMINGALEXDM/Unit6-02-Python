#!/usr/bin/env python3

# Created By: Alex De Meo
# Date: 03/25/2022
# Description: Generates 10 random numbers then finds the one with the greatest
# value and displays it to the screen.

import random

# This function will find the number with the greatest value in the array of
# 10 numbers
def find_max(ints):
    # This is the variable that will hold the highest value
    largest = -1

    for counter in range(len(ints)):
        # WIll only set "largest" to the number it's comparing it to, if the
        # number is greater than the number it's currently olding
        if largest < ints[counter]:
            largest = ints[counter]
    # Returning to main
    return largest


def main():
    int_arr = []
    # generating random numbers
    for counter in range(10):
        rand_num = random.randint(1, 100)
        # putting the random number into the array
        int_arr.append(rand_num)
        print("Position {} is {}".format(counter, int_arr[counter]))
    # calling the function that will find the max Value
    max_value = find_max(int_arr)
    # displaying results
    print("\nThe max value is {}".format(max_value))


if __name__ == "__main__":
    main()
