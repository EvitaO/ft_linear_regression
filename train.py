#!/usr/bin/python

import matplotlib.pyplot as plt
import sys
import numpy as np

from training_classes import *

options = 0

def help():
	print("Program to train using the data in data.csv")
	print("Usage: python3 train.py [-v/v-normalized]")
	print("-v			to display datapoints and linear regresssion line in a graph")
	print("-v-normalized		to display normalized datapoints and normalized linear regresssion line in a graph")
	print("Only one flag at a time can be used")

def setOptions():
	global options
	for arg in sys.argv:
		if arg == "train.py":
			continue
		if arg == "-v":
			options = 1
		elif arg == "-v-normalized":
			options = 2
		elif arg == "-h":
			help()
			exit(0)
		else:
			continue

def getVisuals(km, price, theta0, theta1):
	if km[0] <= 1.0:
		x = np.linspace(0, 1.0, 10)
		plt.text(0.05, 0.05, "y = %.4f - %.4fx" %(theta0, theta1*-1), color='g')
		plt.title("Normalized price vs mileage of a car")
		plt.ylim(0)
	else:
		x = np.array(range(300000))
		plt.title("Relationship between price and mileage of a car")
		plt.text(20000, 2500, "y = %.4f - %.4fx" %(theta0, theta1*-1), color='g')
	y = theta1 * x + theta0
	plt.scatter(km, price, label="data points")
	plt.plot(x, y, color='g', label="linear regression on data points")
	plt.xlabel("Mileage")
	plt.ylabel("Price")
	plt.legend(loc="upper right")
	plt.show()

def main():
	setOptions()

	data = DataHandler()
	data.readfile()
	data.normalize()

	model = LinearRegression(data.km_normalized, data.price_normalized)
	model.calculateLearningRate()
	model.calculate()

	if options == 2:
		getVisuals(data.km_normalized, data.price_normalized, model.theta0, model.theta1)
	
	model.adjustThetas(data.km, data.price)
	model.saveThetas()

	if options == 1:
		getVisuals(data.km, data.price, model.theta0, model.theta1)
	
	x = np.array(range(len(model.error)))
	plt.plot(x, model.error)
	plt.show()

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		plt.close()
		sys.exit(0)