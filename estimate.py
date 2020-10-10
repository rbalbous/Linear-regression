import csv

def read_thetas():
	f = open("thetas.txt", "r")
	thetas = f.read().split("\n")
	try:
		mileage = float(input("Enter the mileage :\n"))
	except:
		print("Please enter a valid mileage")
		exit(0)
	if mileage < 0:
		print("Please enter a valid mileage")
		exit(0)
	return (float(thetas[0]), float(thetas[1]), mileage)

def main():
	theta_0, theta_1, mileage = read_thetas()
	print("The price is : " + str(mileage * theta_1 + theta_0))

if __name__ == "__main__":
	main()
