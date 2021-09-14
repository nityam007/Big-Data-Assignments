#!/usr/bin/env python3
 
import sys
import simplejson as json
 
out = {}
for line in sys.stdin:
	line = line.strip()
	print(line)
	vals = line.split()
	print(vals)
	
	n = len(val)
	
	if(n==4):
		
		val[0]=val[0]+" "+val[1]
		val.pop(val[1])
		
		if(val[1] not in out):
			  
		
		
	
	else:
		p=""
		
		
	for i in vals:
		if(i==str and i not in out):
			out[i]=1
    
		else:
        		out[i]=out[i]+1
			
