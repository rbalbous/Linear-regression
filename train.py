import csv
import math

def train(tab_m, tab_p):
	theta_0, theta_1 = 0, 0
	learning_rate = 0.3
	for m in range(720):
		tmp_0, tmp_1 = 0, 0
		for i in range(len(tab_m)):
			tmp_0 += ((theta_0 + theta_1 * tab_m[i]) - tab_p[i])
			tmp_1 += (((theta_0 + (theta_1 * tab_m[i])) - tab_p[i]) * tab_m[i])
		theta_0 -= learning_rate * (tmp_0 / len(tab_m))
		theta_1 -= learning_rate * (tmp_1 / len(tab_m))
	return theta_0, theta_1

def norm(tab_m):
	min_m = min(tab_m)
	max_m = max(tab_m)
	for i in range(len(tab_m)):
		tab_m[i] = (tab_m[i] - min_m) / (max_m - min_m)
	return(tab_m)

def put_in_file(theta_0, theta_1):
	with open('thetas.csv', 'w') as file:
		print_file = csv.writer(file)
		print_file.writerow([theta_0, theta_1])


def main():
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
	tab_m = norm(tab_m)
	tab_p = norm(tab_p)
	theta_0 , theta_1 = train(tab_m, tab_p)
	put_in_file(theta_0, theta_1)

if __name__ == "__main__":
	main()