#!/usr/bin/python

from train import readfile, estimatePrice
from predict import getThetas

def main():
	km, price = readfile()
	theta0, theta1 = getThetas()

	tmp, tmp1 = 0, 0
	for i,j in zip(km, price):
		estimate = estimatePrice(int(i),float(theta0),float(theta1))
		tmp += abs(int(j) - float(estimate))/int(j)
		tmp1 += (int(j) - float(estimate))/int(j)

	MAPE = (float(tmp)/len(km)*100)
	MPE = (float(tmp1)/len(km)*100)

	print("Mean absolute percentage error is " + "{:.2f}".format(MAPE) + "%")
	print("Mean percentage error is " + "{:.2f}".format(MPE) + "%")

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		sys.exit(0)