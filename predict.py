#!/usr/bin/python

import sys
import os.path
from train import estimatePrice

def help():
    print("\nTo predict a price enter a valid mileage")
    print("Valid mileages are whole numbers and bigger/equal to 0\n")

def getInput():
    mileage = input("Enter a mileage\n")
    try:
        mileage = int(mileage)
    except ValueError:
        help()
        getInput()
    return mileage
        
def getThetas():
    if os.path.exists("thetas.txt"):
        f = open("thetas.txt", "r")
        theta0 = f.readline()
        theta1 = f.readline()
    else:
        theta0 = "0"
        theta1 = "0"
    f.close()
    return theta0, theta1

def main():
    theta0, theta1 = getThetas()
    mileage = getInput()
    price = estimatePrice(mileage, float(theta0), float(theta1))
    if price < 0:
        print("Price for this mileage is: 0.00")
    else:
        print("Price for this mileage is: " + "{:.2f}".format(price))

if __name__ == "__main__":
    try:
	    main()
    except KeyboardInterrupt:
        sys.exit(0)