#!/usr/bin/python

import math
import os.path

class DataHandler:
	def __init__(self):
		self.km = []
		self.price = []
		self.km_normalized = []
		self.price_normalized = []
	
	def filecheck(self):
		if not os.path.exists("data.csv"):
			print("data.csv file is not present in root directory")
			exit(0)
		if os.stat("data.csv").st_size == 0:
			print("data.csv file is empty")
			exit(0)

	def readfile(self):
		self.filecheck()
		file = open("data.csv")
		next(file)
		for line in file:
			data = line.split(',')
			if len(data) != 2 or data[0] == '' or data[1] == '':
				print("data in data.csv file has not the right format")
				exit(0)
			self.km.append(int(data[0]))
			self.price.append(int(data[1]))
		if len(self.km) <= 1 or len(self.price) <= 1:
			print("data.csv file does not contain enough data")
			exit(0)
		file.close()
	
	def calculateNormalized(self, value, dataset):
		return (value - min(dataset)) / (max(dataset) - min(dataset))

	def normalize(self):
		for i, j in zip(self.km, self.price):
			self.km_normalized.append(self.calculateNormalized(i, self.km))
			self.price_normalized.append(self.calculateNormalized(j, self.price))

class LinearRegression:
	def __init__(self, km_normalized=[], price_normalized=[], theta0=0, theta1=0, learningRate=0):
		self.km = km_normalized
		self.price = price_normalized
		self.theta0 = theta0
		self.theta1 = theta1
		self.learningRate = learningRate
		self.error = []

	def calculateLearningRate(self):
		n = len(self.km)
		x = y = y2 = x2 = xy = 0
		for i, j in zip(self.km, self.price):
			x += i
			y += j
			xy += (i*j)
			x2 += (i*i)
			y2 += (j*j)
		self.learningRate = ((n*xy - (x*y)) / math.sqrt((n*x2 - x*x) * (n*y2 - y*y))) * -1
	
	def estimatePrice(self, mileage):
		return self.theta0 + self.theta1 * mileage
	
	def calculate(self):
		tmp0 = 0
		tmp1 = 0
		for i in range(1000):
			tmp0, tmp1 = self.calculateTheta()
			self.theta0 -= tmp0
			self.theta1 -= tmp1
			if i > 1 and self.error[i] == self.error[i-1]:
				break

	def	calculateTheta(self):
		tmp_theta0 = 0
		tmp_theta1 = 0
		error = 0

		for i,j in zip(self.km, self.price):
			tmp_theta0 += (self.estimatePrice(i) - j)
			tmp_theta1 += ((self.estimatePrice(i) - j) * i)
			error += (self.estimatePrice(i) - j)**2

		self.error.append(error/len(self.km))
		tmp_theta0 = self.learningRate * tmp_theta0/len(self.km)
		tmp_theta1 = self.learningRate * tmp_theta1/len(self.price)
		return tmp_theta0, tmp_theta1
	
	def adjustThetas(self, km_original, price_original):
		self.theta1 = (max(price_original) - min(price_original)) / (max(km_original) - min(km_original)) * self.theta1
		self.theta0 = min(price_original) + (max(price_original) - min(price_original)) * self.theta0 + self.theta1 * (1-min(km_original))

	def saveThetas(self):
		f = open("thetas.txt", "w")
		f.write(str(self.theta0) + "\n")
		f.write(str(self.theta1))