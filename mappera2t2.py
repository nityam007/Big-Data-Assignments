#!/usr/bin/env python3

import sys

v_filepath = sys.argv[0]
emb_filepath = sys.argv[1]

emb_file = open(emb_filepath, 'r') 
v_file = open(v_filepath, 'r') 


for line in sys.stdin:
    data=line.strip()
    a=data.split('\t') 
    print(a)
