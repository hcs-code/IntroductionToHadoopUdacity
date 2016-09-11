#!/usr/bin/python

import sys
import csv

def mapper():
	# Using a reader in order to read the whole file
	reader = csv.reader(sys.stdin, delimiter='\t')
	# Jump to the next line. We want to avoid the line with the name of the fields
	reader.next()
	# loop
	for line in reader:
		# Checking no. of fields are correct
    		if len(line) == 19:
			node_id=line[0]
			body=line[4]
			parent_id=line[6]
        		print "{0}\t{1}\t{2}".format(node_id, parent_id, len(body))


mapper()
