#!/usr/bin/python

#!/usr/bin/python

# Code developed by Hector Cobos
# This MapReduce consists on getting the top 10 tags more used in the forum
# In this reducer we have to get all the tags obtained from the mapper.
# After that we have to establish an array with this format [tag,nTimes]
# Finally we get the top 10 ordered by nTimes.
# IN THIS CASE WE ARE ONLY TAKING INTO ACCOUNT type QUESTION.

import sys

count = 0
oldTag = None
arrayTags = []

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    curTag, type = data_mapped
    if type == "question":
    	if oldTag and oldTag != curTag:
		arrayTags.append([count, oldTag])
        	oldTag = curTag
        	count = 0

    	oldTag = curTag
    	count += 1

if type == "question":
    if oldTag != None:
    	arrayTags.append([count,oldTag])

arrayTags=sorted(arrayTags, reverse=True)[0:10]
arrayTags=sorted(arrayTags, reverse=True)

for record in arrayTags:
	print "{0}\t{1}".format(record[1],record[0])

