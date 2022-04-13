#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np

class Plotter:
	def __init__(self, x, y, theta0=0, theta1=0):
		self.x = x
		self.y = y
		self.theta0 = theta0
		self.theta1 = theta1

	def plotNormalized(self):
		x = np.linspace(0, 1.0, 10)
		y = self.theta1 * x + self.theta0
		plt.title("Normalized price vs mileage of a car")
		plt.ylabel("Price")
		plt.xlabel("Mileage")
		plt.scatter(self.x, self.y, label="data points")
		plt.plot(x, y, color='g', label="linear regression on data points")
		plt.text(0.05, 0.05, "y = %.4f - %.4fx" %(self.theta0, self.theta1*-1), color='g')
		plt.ylim(0)
		plt.legend(loc="upper right")
		plt.show()

	def plotOriginal(self):
		x = np.array(range(300000))
		y = self.theta1 * x + self.theta0
		plt.title("Relationship between price and mileage of a car")
		plt.xlabel("Mileage")
		plt.ylabel("Price")
		plt.scatter(self.x, self.y, label="data points")
		plt.plot(x, y, color='g', label="linear regression on data points")
		plt.text(20000, 2500, "y = %.4f - %.4fx" %(self.theta0, self.theta1*-1), color='g')
		plt.legend(loc="upper right")
		plt.show()
	
	def plotError(self):
		plt.title("MSE vs iterations")
		plt.xlabel("iterations")
		plt.ylabel("MSE")
		plt.plot(self.x, self.y)
		plt.show()



