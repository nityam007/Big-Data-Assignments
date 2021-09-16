#!/usr/bin/env python3

#If any of the required attributes contain NaN, ignore the record

import json
import sys
import requests
from datetime import datetime



LATI=float(sys.argv[1]) 
LONGI=float(sys.argv[2])
RASTA=float(sys.argv[3])

for l in sys.stdin:
    
    res=json.loads(l.strip())
    start_lat=(res['Start_Lat'])
    
    
    start_lng=(res['Start_Lng'])
    
    start_lng=float(start_lng)
    start_lat=float(start_lat)
    
    
    
    if start_lng=='NaN' and start_lat=='NaN':
    
       #apna kaam krna 
      continue
    d_NEW=((start_lat-LATI)**2 + (start_lng-LONGI)**2)**0.5
    if(float(d_NEW)<RASTA):
    
    
    
    
        data={"latitude":start_lat,"longitude":start_lng}
        
        
        
        readed=requests.post(url="http://20.185.44.219:5000/",json=data)
        
        
        
        
        
        
        
        
        
        
        
        readed_new=readed.json()
        
        # print(readed_new['city'],readed_new['state'],1)
        print("{}${}${}".format(readed_new['state'],readed_new['city'],1))
