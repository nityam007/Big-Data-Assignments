#!/usr/bin/env python3

import sys


to_hold={}  #A dictionary to hold the node and the list of nodes it point to.

for line in sys.stdin:
	line = line.strip() # Removing white spaces after every line
	holder = line.split() # Striping lines based on white space
	holder=list(map(int,holder))
	
	if(holder[0] in to_hold):
		to_hold[holder[0]].append(holder[1])
	
	else:
		to_hold[holder[0]]=[holder[1]]
	
fptr = open(r"v.txt","w")

for k in to_hold:
	fptr.write(str(k))
	fptr.write(",")
	fptr.write("1")
	fptr.write("\n")

for i in to_hold:
	print(i,"\t", to_hold[i]) # Printing with \t as the delimiter (as the same was used in the assignment description as well)
