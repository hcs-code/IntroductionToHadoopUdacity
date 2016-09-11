#!/usr/bin/python

# Developed by Hector Cobos

import sys
import csv
import datetime

def mapper():
	# Using a reader in order to read the whole file
	reader = csv.reader(sys.stdin, delimiter='\t')
	# Jump to the next line. We want to avoid the line with the name of the fields
	reader.next()
	# loop
	for line in reader:
		# Checking no. of fields are correct
    		if len(line) == 19:
			author_id=line[3]
			date=line[8]
			time = date.strip().split(" ")
			hour = time[1].strip().split(":")
        		print "{0}\t{1}".format(author_id, hour[0])


mapper()
