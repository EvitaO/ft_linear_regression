#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
import math
import sys


options = 0
learningRate = 0

def readfile():
	file = open("data.csv")
	next(file)
	x = []
	y = []
	for line in file:
		xy = line.split(',')
		x.append(int(xy[0]))
		y.append(int(xy[1]))
	file.close()
	return x,y

def calculateNorm(value, dataset):
	return (value - min(dataset))/(max(dataset)-min(dataset))

def	normalize(x, y):
	normalized = []
	for i,j in zip(x,y):
		normalized.append([calculateNorm(float(i), x), calculateNorm(float(j), y)])
	return normalized

def splitNormalize(data):
	price = []
	km = []
	for i in data:
		km.append(i[0])
		price.append(i[1])
	return km, price

def calculateLearningRate(km, price):
	n = len(km)
	x = y = y2 = x2 = xy = 0
	for i, j in zip(km, price):
		x += i
		y += j
		xy += (i*j)
		x2 += (i*i)
		y2 += (j*j)
	global learningRate
	learningRate = (n*xy - (x*y)) / math.sqrt((n*x2 - x*x) * (n*y2 - y*y))
	learningRate = learningRate * -1


def estimatePrice(mileage, theta0, theta1):
	return theta0 + (theta1 * mileage)

def calculate(km, price):
	tmp0 = 0
	tmp1 = 0
	theta0 = 0
	theta1 = 0
	for i in range(1000):
		tmp0, tmp1 = calculateTheta(km, price, theta0, theta1)
		theta0 -= tmp0
		theta1 -= tmp1
	return theta0, theta1

def	calculateTheta(km, price, theta0, theta1):
	tmp = 0
	tmp1 = 0
	t0 = 0
	t1 = 0

	for i,j in zip(km, price):
		tmp = (estimatePrice(i, theta0, theta1) - j)
		tmp1 = ((estimatePrice(i, theta0, theta1) - j) * i)
		t0 += tmp
		t1 += tmp1
	t0 = learningRate * t0/len(km)
	t1 = learningRate * t1/len(price)
	return t0, t1

def denormalizeThetas(x, y, theta0, theta1):	
	theta0 = theta0 * (max(y) - min(y)) + min(y)
	theta1 = (y[0] - theta0) / x[0]
	return theta0, theta1

def saveThetas(theta0, theta1):
	f = open("thetas.txt", "w")
	f.write(str(theta0) + "\n")
	f.write(str(theta1))

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
		x = np.linspace(0, 1, 11)
	else:
		x = np.array(range(300000))
	y = theta1 * x + theta0
	plt.scatter(km, price)
	plt.plot(x, y)
	plt.show()

def	processData():
	x,y = readfile()
	normalized = normalize(x,y)
	km, price = splitNormalize(normalized)

	calculateLearningRate(km, price)
	theta0, theta1 = calculate(km, price)

	if options == 2:
		getVisuals(km, price, theta0, theta1)

	theta0, theta1 = denormalizeThetas(x, y, theta0, theta1)
	saveThetas(theta0, theta1)

	if options == 1:
		getVisuals(x, y, theta0, theta1)

def main():
	setOptions()
	processData()

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		sys.exit(0)