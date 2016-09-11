#!/usr/bin/python

# This MapReduce consists on getting the hours when the students are more active on the forum.
# The first thing we have to do is to order by hour and obtaining an array of hours like this [05,12,12,14]
# Then we have to prepare an array of popular hours because it could be that the student could have two or more
# popular hours. Once we have the array of popular hours, we have only to print them with the associate student.

import sys, string

arrayNodes = []
arrayAnswers = []

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 3:
        # Something has gone wrong. Skip this line.
        continue

    node_id, parent_id, lgt = data_mapped

    if parent_id == "\N":
    	arrayNodes.append([node_id,lgt])
    else:
	arrayAnswers.append([parent_id,lgt])

for node in arrayNodes:
    n=0
    totalLength=0.0
    for record in arrayAnswers:
    	node2=record[0]
    	longt2=record[1]

	if node[0]==node2:
	    totalLength=float(totalLength+int(longt2))
       	    n+=1
    if n==0:
	print "{0}\t{1}\t{2}".format(node[0],node[1], 0)
    else:
	print "{0}\t{1}\t{2}".format(node[0],node[1], float(totalLength/n))


