#!/usr/bin/env python3

import sys
import json

v_filepath = sys.argv[2]
emb_filepath = sys.argv[1]

# print(
emb_file = open(emb_filepath, 'r') 
v_file = open(v_filepath, 'r') 


lines = []
lines = v_file.readlines()

count = 0
all_nodes=[]
for line in lines:
    print(line)
    all_nodes.append(line[0])
    count += 1

print(all_nodes)

rows, cols = (count, count)
 
TransMat = [[0]*cols]*rows

for i in TransMat:
    	for j in range(0,len(i)): 
    		print(i[j-1],end=" ")
    	print("\n")

mover=0

for line in sys.stdin:
    data=line.strip()
    a=data.split('\t') 
    
    to_strip=a[1].strip('][ ').split(', ')
    to_strip=list(to_strip)
    lengths=list(map(int,to_strip))
    print(lengths)
    

    for j in range(0,count):
    	if (j+1) not in lengths:
    		TransMat[mover][j-1]=0
    		
    	else:
    		TransMat[mover][j]=1/(len(lengths)) 
    		print(len(lengths))
    mover+=1
    		
for i in TransMat:
    	for j in range(0,len(i)): 
    		print(i[j-1],end=" ")
    	print("\n")
