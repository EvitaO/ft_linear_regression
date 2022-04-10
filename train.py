#!/usr/bin/python

from re import A, X
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

def calculate(km, price):
	tmp0 = 0
	tmp1 = 0
	global theta0
	global theta1
	for i in range(300000):
		tmp0, tmp1 = calculateTheta(km, price)
		theta0 -= tmp0
		theta1 -= tmp1

def	calculateTheta(km, price):
	tmp = 0
	tmp1 = 0
	t0 = 0
	t1 = 0

	for i,j in zip(km, price):
		tmp = (estimatePrice(i) - j)
		tmp1 = ((estimatePrice(i) - j) * i)
		t0 += tmp
		t1 += tmp1
	t0 = learningRate * t0/len(km)
	t1 = learningRate * t1/len(price)
	return t0, t1

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

	calculate(km, price)

	global theta0
	global theta1

	print(theta0)
	print(theta1)

	theta0 = theta0 * max(y)
	theta1 = (y[0] - theta0) / x[0]
	
	print(theta0)
	print(theta1)

	x = np.array(range(300000))
	y = theta1 * x + theta0
	plt.plot(x, y)
	plt.show()

if __name__ == "__main__":
	main()