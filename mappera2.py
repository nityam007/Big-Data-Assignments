#!/usr/bin/env python3

import sys

for line in sys.stdin:
    data=line.strip()
    a=data.split('\t') 
    a=list(map(int,a))
    
    print(a[0]," ",a[1])
