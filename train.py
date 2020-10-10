import csv
import matplotlib.pyplot as plt
import numpy as np


def train(data, min_km, max_km, min_price, max_price):
	theta_0 = 0.0
	theta_1 = 0.0
	data_len = len(data)
	for i in range(100000):
		sum_t0 = 0.0
		sum_t1 = 0.0
		learning_rate = 0.005
		for item in data:
    			#normalize the dataset to scale
			item_0 = (float(item[0]) - min_km) / (max_km - min_km)
			item_1 = (float(item[1]) - min_price) / (max_price - min_price)

			# Applying the train formula
			sum_t0 = sum_t0 + (theta_0 + (theta_1 * item_0) - item_1)
			sum_t1 = sum_t1 + (theta_0 + (theta_1 * item_0) - item_1) * item_0
		theta_0 -= learning_rate * 1/data_len * sum_t0
		theta_1 -= learning_rate * 1/data_len * sum_t1
	return data, theta_0, theta_1


def denorm(min_km, max_km, min_price, max_price, theta_0, theta_1):
	theta_0 = theta_0 * (max_price - min_price) + min_price - (theta_1 * min_km * (max_price - min_price)) / (max_km - min_km)
	theta_1 = theta_1 * (max_price - min_price) / (max_km - min_km)
	return theta_0, theta_1


def put_in_file(theta_0, theta_1):
	f = open("thetas.txt", "w")
	f.write(str(theta_0) + "\n" + str(theta_1))
	f.close()


def precision(data, theta_0, theta_1, data_len):
	precision = 0
	for item in data:
		estimation = float(item[0]) * theta_1 + theta_0
		if estimation > float(item[1]):
				precision += float(item[1]) / estimation
		else:
			precision += estimation / float(item[1])
	print("precision: " + str(precision / data_len))

def display(data, theta_0, theta_1):
	for item in data:
		plt.scatter(float(item[0]),float(item[1]), color='blue')

	#plotting line
	plot_x = np.linspace(0, 250000, 250000)
	plot_y = theta_1 * plot_x + theta_0
	plt.plot(plot_x, plot_y, '-r')
	plt.xlabel("Mileage")
	plt.ylabel("Price")
	plt.show()


def main():
	with open('data.csv', newline='') as f:
		reader = csv.reader(f)
		data = list(reader)
	f.close()
	data = data[1:]
	data_len = len(data)
	min_km = min(float(x[0]) for x in data)
	max_km = max(float(x[0]) for x in data)
	max_price = max(float(x[1]) for x in data)
	min_price = min(float(x[1]) for x in data)
	data, theta_0, theta_1 =  train(data, min_km, max_km, min_price, max_price)
	theta_0, theta_1 = denorm(min_km, max_km, min_price, max_price, theta_0, theta_1)
	put_in_file(theta_0, theta_1)
	
	# BONUS : Get precision
	precision(data, theta_0, theta_1, data_len)

	#BONUS Display a graph of the linear regression
	display(data, theta_0, theta_1)


if __name__ == "__main__":
	main()
