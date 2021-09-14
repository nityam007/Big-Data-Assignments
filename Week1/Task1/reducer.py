#!/usr/bin/env python3
 
import sys
import simplejson as json
 
 
# initiate output map
output = dict()

# loop through each line for stdin
for line in sys.stdin:
	line = line.strip()
	vals = line.split()
	#print(vals)
	
	if(vals[0] not in output):
		output[(vals[0])]=int(vals[1])
	
	else:
		output[(vals[0])]=output[(vals[0])]+1
	

vals_holder=[]

for i in output:
	vals_holder.append(int(i))

vals_holder.sort()

for i in vals_holder:
	print(i, output[str(i)])
