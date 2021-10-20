#!/usr/bin/env python3

import sys

prev_source = -1
sum=0

for line in sys.stdin:
	line = line.strip()
	temp = line.split()
	source = int(temp[0])
	dest = int(temp[1])
	contr = float(temp[2])
	# source,dest,contr = list(map(float,line.split(';'))) 

	if(source!=prev_source and prev_source!=-1):
		rank = 0.15 + 0.85 * sum
		out = str(prev_source)+','+str(round(rank,2))
		print(out)
		sum=contr
		prev_source=source
	else:
		sum+=contr
		prev_source=source

rank = 0.15 + 0.85 * sum
out = str(prev_source)+','+str(round(rank,2))
print(out)
