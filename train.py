#!/usr/bin/python

from re import X
import matplotlib.pyplot as plt
import numpy as np

theta0 = 0
theta1 = 0
learningRate = 0.5

def readfile():
	file = open("data.csv")
	next(file)
	x = []
	y = []
	for line in file:
		xy = line.split(',')
		x.append(int(xy[0]))
		y.append(int(xy[1]))
	return x,y

def calculateNorm(value, dataset):
	return (value - min(dataset))/(max(dataset)-min(dataset))


def	normalize(x, y):
	normalized = []
	for i,j in zip(x,y):
		normalized.append([calculateNorm(float(i), x), calculateNorm(float(j), y)])
	return normalized

def estimatePrice(mileage):
	return theta0 + (theta1 * mileage)

def	calculateTheta(km, price):
	tmp = 0
	tmp1 = 0
	global theta0
	global theta1

	for i,j in zip(km, price):
		tmp = (estimatePrice(i) - j)
		tmp1 = ((estimatePrice(i) - j) * i)
		theta0 = theta0 - learningRate * (tmp/len(km))
		theta1 = theta1 - learningRate * (tmp1/len(price))
	return theta0, theta1

def	main():
	x,y = readfile()
	normalized = normalize(x,y)
	price = []
	km = []
	for i in normalized:
		km.append(i[0])
		price.append(i[1])
		print (i)
	# plt.scatter(km, price)
	# plt.show()

	theta0, theta1 = calculateTheta(km, price)
	print(theta0)
	print(theta1)
	# formula found using excel
	# y = -0.0214 * x + 8500
	# x = np.array(range(300000))

	# theta0, theta1 = calculateRegressionLine(x, y)
	# print("theta0 = " + str(theta0) + "	theta1 = " + str(theta1))

if __name__ == "__main__":
	main()