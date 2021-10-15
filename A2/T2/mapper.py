#!/usr/bin/env python3

import sys
import json

v_filepath = sys.argv[2]
emb_filepath = sys.argv[1]

# print
emb_file = open(emb_filepath, 'r') ###Page Embedding file
v_file = open(v_filepath, 'r') 



#### S embedding matrix #####
### Similarity calculation is just dot product between two word embeddings

embedding_data=json.loads(emb_file.read()) #This will read it as dictionary


for line in sys.stdin: #Reading from Adjacency List given as input
    data=line.strip()
    a=data.split('\t') #Splitting Adjacency List by Key : Value
    key=a[0].rstrip() #to remove right end spaces
    
    to_strip=a[1].strip('][ ').split(', ') #a[1] is list of values
    to_strip=list(to_strip)
    lengths=list(map(int,to_strip)) #lengths contains all the nodes  key pointing to
   
    for i in lengths: #iterate through every value where key is pointing to calculate similarity between them
         
 	 
	 
	 
	 #dictionary : embedding_data
     #print(type(embedding_data[str(i)]))
     vec_a=embedding_data[str(i)].copy() 	 #one of the node where key is pointing to
     vec_b=embedding_data[key].copy()    #Key which is read from line 
         
	
	 # Dot and norm 
     dot = sum(i*j for i, j in zip(vec_a, vec_b))
     mod_a = sum(i*i for i in vec_a) ** 0.5
     mod_b = sum(j*j for j in vec_b) ** 0.5

	 # Cosine similarity
     cos_sim = dot / (mod_a*mod_b)
     temp_comp=(cos_sim /len(lengths))#multiplying with outgoing probablities (Transition Matrix Values)
     #(node key being pointed - Nodes which point to key -Contribution value)
     print(i," ",a[0]," ",temp_comp) # int string float output with one space separation 
    
    
   
   
    	
  
 
 
 
 
 
 	
	
   
  
