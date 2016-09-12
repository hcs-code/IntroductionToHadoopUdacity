#!/usr/bin/python

# Code developed by Hector Cobos
# This MapReduce consists on getting the top 10 tags more used in the forum

import sys
import csv
import string

def mapper():
	# Using a reader in order to read the whole file
	reader = csv.reader(sys.stdin, delimiter='\t')
	# Jump to the next line. We want to avoid the line with the name of the fields
	reader.next()
	# loop
	for line in reader:
		# Checking no. of fields are correct
    		if len(line) == 19:
                        # Getting node_type and tags
			node_type=line[5]
			tags=line[2]
                        # In one line of tags could be more than one tag. For that reason
                        # we need to split them
			etiquetas=tags.split(" ")
			num=len(etiquetas)
                        # Printing tags
			if num>1:
				for record in etiquetas:
					print "{0}\t{1}".format(record, node_type)
			else:
				print "{0}\t{1}".format(tags, node_type)


mapper()
