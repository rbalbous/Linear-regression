import csv

def main():
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
	price = theta_0 + (theta_1 * mileage)
	print(price)

if __name__ == "__main__":
	main()