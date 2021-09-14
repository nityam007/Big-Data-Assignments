#!/usr/bin/env python3
import sys, json,requests
lat=float(sys.argv[1])
lng=float(sys.argv[2])
d=float(sys.argv[3])
a=0
b=0
for line in sys.stdin:
    line=line.strip()
    res=json.loads(line)
    start_lat=float(res['Start_Lat'])
    start_lng=float(res['Start_Lng'])
    ed=((start_lat-lat)*2 + (start_lng-lng)2)*0.5
    if(float(ed)<d):
        payload={"latitude":start_lat,"longitude":start_lng}
        re=requests.post(url="http://20.185.44.219:5000/",json=payload)
        ev=re.json()
        print(ev['city'],ev['state'],1)
