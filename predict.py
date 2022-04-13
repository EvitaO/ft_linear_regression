#!/usr/bin/python

import sys
import os.path
from training_classes import LinearRegression

def help():
	print("\nTo predict a price enter a valid mileage")
	print("Valid mileages are whole numbers and bigger/equal to 0\n")

def getInput():
	user_input = -1
	while user_input < 0:
		mileage = input("Enter a mileage\n")
		try:
			user_input = int(mileage)
			if user_input < 0:
				raise ValueError()
		except ValueError:
			help()
	return user_input
		
def getThetas():
	if os.path.exists("thetas.txt"):
		f = open("thetas.txt", "r")
		theta0 = f.readline()
		theta1 = f.readline()
		f.close()
	else:
		theta0 = 0.0
		theta1 = 0.0
	return theta0, theta1

def main():
	theta0, theta1 = getThetas()
	mileage = getInput()

	model = LinearRegression(theta0=float(theta0), theta1=float(theta1))
	price = model.estimatePrice(float(mileage))
	if price < 0:
		print("Price for this mileage is: 0.00")
	else:
		print("Price for this mileage is: " + "{:.2f}".format(price))

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		sys.exit(0)