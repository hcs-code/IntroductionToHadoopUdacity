#!/usr/bin/python

import sys

oldNode = None
oldStudent = None
arrayStudents = []

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    curNode, curStudent = data_mapped

    if oldNode and oldNode != curNode:
	arrayStudents=sorted(arrayStudents, reverse=False)
    	print "{0}\t{1}".format(oldNode, arrayStudents)
	arrayStudents = []
	arrayStudents.append(curStudent)	
	oldNode = curNode
    else:
	arrayStudents.append(curStudent)
        
    oldNode = curNode
    oldStudent = curStudent

if oldNode != None:
    print "{0}\t{1}".format(oldNode, arrayStudents)

