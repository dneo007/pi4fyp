# Python program to demonstrate
# writing to CSV


import csv
from datetime import datetime
import time
#start_time = time.time()

def csvoperation(reading):
	# field names
	#fields = ['Name', 'Branch', 'Year', 'CGPA']

	# data rows of csv file
	rows = [ [datetime.now(), reading]]

	# name of csv file
	filename = "newtest.csv"

	# writing to csv file

	with open(filename, 'a') as csvfile:
		# creating a csv writer object
		csvwriter = csv.writer(csvfile)

		# writing the fields
		#	csvwriter.writerow(fields)

		# writing the data rows
		csvwriter.writerows(rows)
		#print("--- %s seconds ---" % (time.time() - start_time))
