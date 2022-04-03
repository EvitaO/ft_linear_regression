#!/usr/bin/python

from re import X


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
		normalized.append([calculateNorm(int(i), x), calculateNorm(int(j), y)])
	return normalized

def	main():
	x,y = readfile()
	normalized = normalize(x,y)
	for i in normalized:
		print (i)
	# theta0, theta1 = calculateRegressionLine(x, y)
	# print("theta0 = " + str(theta0) + "	theta1 = " + str(theta1))

if __name__ == "__main__":
	main()