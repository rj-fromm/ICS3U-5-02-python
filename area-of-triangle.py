#!/usr/bin/env python3

# Created by: RJ Fromm
# Created on: november 2019
# This show two functions


def calculate_area(base, height):
    # process
    area = (base*height)/2
    print("The area is {0}".format(area))


def main():
    while True:
        base_of_triangle = input("Enter the base of the traingle: ")
        height_of_triangle = input("Enter the height of the traingle: ")
        try:
            base_user_int = int(base_of_triangle)
            height_user_int = int(height_of_triangle)

            calculate_area(base_user_int, height_user_int)
            break
        except Exception:
            print("that is not a number")


if __name__ == "__main__":
    main()
