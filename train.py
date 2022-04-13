#!/usr/bin/python

import sys
from training_classes import *
from visual import *

options = 0

def help():
	print("Program to calculate a linear regression equation using the data in data.csv")
	print("Usage: python3 train.py [flags]")
	print("Possible flags:")
	print("-v-normalized		to display normalized datapoints and normalized linear regresssion line in a graph")
	print("-v			to display datapoints and linear regresssion line in a graph")
	print("-e			to display the MSE vs iterations in a graph")

def setOptions():
	global options
	for arg in sys.argv:
		if arg == "train.py":
			continue
		if arg == "-v-normalized":
			options |= 1 << 0
		elif arg == "-e":
			options |= 1 << 1
		elif arg == "-v":
			options |= 1 << 2
		elif arg == "-h":
			help()
			exit(0)
		else:
			continue

def main():

	setOptions()

	data = DataHandler()
	data.readfile()
	data.normalize()

	model = LinearRegression(data.km_normalized, data.price_normalized)
	model.calculateLearningRate()
	model.calculate()

	theta0_normalized = model.theta0
	theta1_normalized = model.theta1
	
	model.adjustThetas(data.km, data.price)
	model.saveThetas()

	if options & (1<<0):
		normalizedGraph = Plotter(data.km_normalized, data.price_normalized, theta0_normalized, theta1_normalized)
		normalizedGraph.plotNormalized()
	if options & (1<<1):
		error = Plotter(range(len(model.error)), model.error)
		error.plotError()
	if options & (1<<2):
		graph = Plotter(data.km, data.price, model.theta0, model.theta1)
		graph.plotOriginal()
	

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		plt.close()
		sys.exit(0)