#!/usr/bin/env python3

import sys
import os
 

temp=None 
source_node_checker=0

holding_list=[]
# path= os.getcwd()+"/v"
path="/home/pes_bigdata/Desktop/Assignment-2/v"
fptr = open(path,"w")

for line in sys.stdin:
	line = line.strip() # Removing white spaces after every line
	holder = line.split() # Striping lines based on white space
	holder=list(map(int,holder))
	
	source_node_checker=holder[0]
	
	if(temp==None):
		temp=holder[0]
		holding_list.append(holder[1])
		fptr.write(str(temp))
		fptr.write(",")
		fptr.write("1")
		fptr.write("\n")
		
	elif(temp==source_node_checker):
		holding_list.append(holder[1])
		
	elif(temp!=source_node_checker):
		print("%s\t" %temp, end="")
		print(holding_list)
		
		holding_list=[]
		holding_list.append(holder[1])
		fptr.write(str(source_node_checker))
		fptr.write(",")
		fptr.write("1")
		fptr.write("\n")
	
	
	temp=source_node_checker
	
	
print("%s\t" %temp, end="")
print(holding_list)	

fptr.close()
