#!/usr/bin/env python3

import json
import sys
from datetime import datetime

key1='lane blocked'
key2='shoulder blocked'
key3='overturned vehicle'

vals={}
temp=[]
for line in sys.stdin:
    data=json.loads(line.strip())
    a=data['Description'].strip()

    if( (key1 in a.lower()) or (key2 in a.lower()) or (key3 in a.lower()) ):
        if(data['Severity']>=2):
            if(data['Visibility(mi)']<=10):
                if(data['Precipitation(in)']>=0.2):
                    if( (data['Weather_Condition']=='Heavy Snow') or (data['Weather_Condition']=='Thunderstorm') or (data['Weather_Condition']=='Heavy Rain') or   (data['Weather_Condition']=='Heavy Rain Showers')  or (data['Weather_Condition']=='Blowing Dust') ):
                        if(data['Sunrise_Sunset']=='Night'):
                            #print(data['ID'])
                            held=data["Start_Time"].split()
                            new_held=held[1].split(':')
                            temp.append(int(new_held[0]))
                            #time=datetime.strptime(data["Start_Time"].strip(),"%Y-%m-%d %H:%M:%S")
                            #temp.append(time.hour)
temp.sort()
for i in temp:
   print("%s\t%s"%(i,1))
