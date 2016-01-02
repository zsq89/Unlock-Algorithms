import matplotlib.pyplot as plt
from math import pow
import sys

def getMaxBeer(pay):
	PRICE = 2
	CAPVALUE = 4
	BOTVALUE = 2

	beer = 0
	cap = 0
	bot = 0

	paid = divmod(pay, PRICE)[0]
	beer = paid
	cap = paid
	bot = paid

	while cap > 3 or bot > 1:
		capRes = divmod(cap, CAPVALUE)
		botRes = divmod(bot, BOTVALUE)
		newBeer = capRes[0] + botRes[0]
		beer += newBeer
		cap = capRes[1] + newBeer
		bot = botRes[1] + newBeer

	return beer

def main():
	beer = getMaxBeer(10)
	print("10 dollars can drink " + str(beer) + " beers")
	beer = getMaxBeer(100)
	print("100 dollars can drink " + str(beer) + " beers")
	beer = getMaxBeer(500)
	print("500 dollars can drink " + str(beer) + " beers")

	x=[]
	y=[]
	for num in range(0, 9):
		x.append(num)
		y.append(getMaxBeer(pow(10, num)))

	plt.scatter(x,y)
	plt.show()

if __name__ == '__main__':
	sys.exit(main())
