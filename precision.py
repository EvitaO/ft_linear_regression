#!/usr/bin/python

from training_classes import *
from predict import getThetas

"""
Mean absolute error shows the average error
Mean square error shows the average square error
Mean absolute percentage error shows the MAE but in percentages
Mean percentage error shows if there are more positive or negative errors in percentages
"""

def calculatePrecision(km, price, theta0, theta1):
	mape, mpe, mae, mse = 0, 0 ,0, 0
	model = LinearRegression(theta0=float(theta0), theta1=float(theta1))
	for i,j in zip(km, price):
		estimate = model.estimatePrice(int(i))
		mape += abs(int(j) - float(estimate))/int(j)
		mpe += (int(j) - float(estimate))/int(j)
		mae += abs(int(j) - float(estimate))
		mse += pow((int(j) - float(estimate)), 2)

	mape = (float(mape)/len(km)*100)
	mpe = (float(mpe)/len(km)*100)
	mae = mae/len(km)
	mse = mse/len(km)
	return mape, mpe, mae, mse

def main():
	data = DataHandler()
	data.readfile()
	theta0, theta1 = getThetas()

	mape, mpe, mae, mse = calculatePrecision(data.km, data.price, theta0, theta1)
	
	print("Mean absolute error is " + "{:.2f}".format(mae))
	print("Mean square error is " + "{:.2f}".format(mse))
	print("Mean absolute percentage error is " + "{:.2f}".format(mape) + "%")
	print("Mean percentage error is " + "{:.2f}".format(mpe) + "%")

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		sys.exit(0)