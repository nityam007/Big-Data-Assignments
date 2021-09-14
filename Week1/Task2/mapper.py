import json
import sys
from datetime import datetime

import requests

URL='http://20.185.44.219:5000/'

Start_Lat=sys.argv[1]
Start_Lng=sys.argv[2]
#D=sys.argv[3]
#print(Start_Lat)
n = len(sys.argv)
myojb={"latitude": Start_Lat,
    "longitude": Start_Lng}
r=requests.post( url=URL, json=myojb)
data=r.json()

    
print(data)