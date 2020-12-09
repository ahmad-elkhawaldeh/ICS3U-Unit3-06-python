#!/usr/bin/env python3

# Created by: Ahmad el-khawaldeh
# Created on: December 2020
# This program generates a random number so  the user can guess what the number is 

import random

random_number = random.randint(1, 10)


def main():
    # this function sees if the user iputed the random number

    print("enter a number from 1 to 10")

    # input
    User_number_string = input("Enter an integer: ")

    # process
    try:
        User_number = int(User_number_string)
        random_number == random.randint(1, 10)

        if User_number == random_number:
            # output
            print(" Correct   ")
        else:
            # Output
            print(" incorrect ")
            print(" the corect answer was: {}".format(random_number))

    except Exception:
        print("This was not an integer")


if __name__ == "__main__":
    main()
