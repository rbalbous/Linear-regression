import csv

def read_thetas():
	with open('thetas.csv') as file:
		tab = csv.reader(file)
		for item in tab:
			theta_0 = float(item[0])
			theta_1 = float(item[1])
	while (1):
		try:
			mileage = float(input("Enter the mileage :\n"))
		except:
			print("Please enter a valid mileage")
			continue
		if mileage < 0:
			print("Please enter a valid mileage")
		else:
			break
	return (theta_0, theta_1, mileage)

def get_price(mileage, theta_0, theta_1):
	tab_m = []
	tab_p = []
	with open('data.csv') as file:
		tab = csv.reader(file)
		for item in tab:
			try:
				tab_m.append(float(item[0]))
				tab_p.append(float(item[1]))
			except:
				continue
	min_m = min(tab_m)
	max_m = max(tab_m)
	min_p = min(tab_p)
	max_p = max(tab_p)
	mileage = (mileage - min_m) / (max_m - min_m)
	price = ((theta_0 + theta_1 * mileage)) * (max_p - min_p) + min_p
	return (price)

def main():
	theta_0, theta_1, mileage = read_thetas()
	price = get_price(mileage, theta_0, theta_1)
	if price < 0:
		price = 0
	print("The price is :", int(price))

if __name__ == "__main__":
	main()