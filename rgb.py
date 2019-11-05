#!/usr/bin/env python3

# Created by: Amir Mersad
# Created on: November 2019
# This program prints all RGB numbers


def main():
    # This function prints all RGB numbers

    # Process
    for red in range(0, 255):
        for green in range(0, 255):
            for blue in range(0, 255):
                # Output
                print("RGB({0},{1},{2})".format(red, green, blue))


if __name__ == "__main__":
    main()
