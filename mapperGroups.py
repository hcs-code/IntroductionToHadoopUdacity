#!/usr/bin/python

# Developed by Hector Cobos
# This MapReduce consists on getting the parent nodes and establish all the students who have
# been participating in that post.

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
			author_id=line[3]
			parent_id=line[6]
			if parent_id == '\N':
				print "{0}\t{1}".format(node_id, author_id)
			else:
				print "{0}\t{1}".format(parent_id, author_id)


mapper()
