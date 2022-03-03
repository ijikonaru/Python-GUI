# testcsv.py

import csv

def writetocsv(data):
	with open('data.csv','a',newline='',encoding='utf-8') as file:
		fw = csv.writer(file) # fw = file writer
		fw.writerow(data)




data = ['Banana',100,dtime]
writetocsv(data)





