import csv

def is_login(username, password):
	with open('data.csv') as f:
		for i in csv.reader(f):
			if i[1] == username and i[2] == password:
				return i[0]
		else:
			return None
