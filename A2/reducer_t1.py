#!/usr/bin/env python3

import sys


to_hold={}  #A dictionary to hold the node and the list of nodes it point to.

temp=None 
source_node_checker=0

holding_list=[]
for line in sys.stdin:
	line = line.strip() # Removing white spaces after every line
	holder = line.split() # Striping lines based on white space
	holder=list(map(int,holder))
	
	source_node_checker=holder[0]
	
	if(temp==None):
		temp=holder[0]
		holding_list.append(holder[1])
	
	elif(temp==source_node_checker):
		holding_list.append(holder[1])
		
	elif(temp!=source_node_checker):
		print(temp,"\t", holding_list)
		holding_list=[]
		holding_list.append(holder[1])
	
	
	temp=source_node_checker
	
print(temp,"\t",holding_list)	
	
fptr = open(r"v.txt","w")

for k in to_hold:
	fptr.write(str(k))
	fptr.write(",")
	fptr.write("1")
	fptr.write("\n")

fptr.close()
