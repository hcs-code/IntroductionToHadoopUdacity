#!/usr/bin/python

# Developed by Hector Cobos

# This MapReduce consists on getting the hours when the students are more active on the forum.
# The first thing we have to do is to order by hour and to obtain an array of hours like this [05,12,12,14]
# Then we have to prepare an array of popular hours because it could be the student could have two or more
# popular hours. Once we have the array of popular hours, we have only to print it with the associate student.

import sys

# Variables
oldUser = None
oldHour = None
arrayHours = []
arrayPopularHours = []
maxValue = 0


for line in sys.stdin:

    # Reading values from Mapper
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    currentUser, currentHour = data_mapped

    if oldUser and oldUser != currentUser:
        arrayHours=sorted(arrayHours, reverse=False)
	i=0
	for horas in arrayHours:
		value=arrayHours[i]
		nTimes=arrayHours.count(value)
		if nTimes > maxValue:
			maxValue = nTimes
			arrayPopularHours = []
			arrayPopularHours.append(value)
		elif nTimes == maxValue:
			c=arrayPopularHours.count(value)
			if c==0:
				arrayPopularHours.append(value) 
		i+=1
	j=0
	for p in arrayPopularHours:
		print oldUser, "\t", arrayPopularHours[j]
		j+=1

	# Inicialising for the next student
	arrayPopularHours = []
	maxValue = 0
	arrayHours = []

    arrayHours.append(currentHour)
    oldUser = currentUser
    oldHour = currentHour

# Printing last student
if oldUser != None:
        arrayHours=sorted(arrayHours, reverse=False)
	i=0
	for horas in arrayHours:
		value=arrayHours[i]
		nTimes=arrayHours.count(value)
		if nTimes > maxValue:
			maxValue = nTimes
			arrayPopularHours = []
			arrayPopularHours.append(value)
		elif nTimes == maxValue:
			c=arrayPopularHours.count(value)
			if c==0:
				arrayPopularHours.append(value) 
		i+=1
	j=0
	for p in arrayPopularHours:
		print oldUser, "\t", arrayPopularHours[j]
		j+=1

