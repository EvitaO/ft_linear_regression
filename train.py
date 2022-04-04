#!/usr/bin/python

from re import X
import matplotlib.pyplot as plt


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

def	main():
	x,y = readfile()
	normalized = normalize(x,y)
	price = []
	km = []
	for i in normalized:
		km.append(i[0])
		price.append(i[1])
		print (i)
	plt.scatter(km, price)
	plt.show()
	# theta0, theta1 = calculateRegressionLine(x, y)
	# print("theta0 = " + str(theta0) + "	theta1 = " + str(theta1))

if __name__ == "__main__":
	main()