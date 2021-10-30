import csv
import sys

country=sys.argv[1]
#print(sys.argv[0])
path='/Users/Darshilshah/Downloads/city_sample_5percent.csv'
city_gtt_avgtemp=dict()
city_avgtemp=dict()
file=open(path,"r")
data=file.read()
i=0
with open(path) as csv_file:

    csv_reader=csv.reader(csv_file)

    for line in csv_reader:
        if(line[4]==country):
            
            if(line[3] in city_avgtemp):
                try:
                    city_avgtemp[line[3]]+=float(line[1])
                except:
                    i+=1          
            
            else:
                try:
                    city_avgtemp[line[3]]=float(line[1])
                except:
                    i+=1
                
    for x in city_avgtemp:
         occurences=data.count(x)
         city_avgtemp[x]=city_avgtemp[x]/occurences
            


with open(path) as csv_file2:
    csv_reader=csv.reader(csv_file2)
    for line2 in csv_reader:
        if(line2[4]==country): 
            try:
                if((float(line2[1])>city_avgtemp[line2[3]])):
                    city_gtt_avgtemp[line2[3]]+=1
                    
                else:
                    city_gtt_avgtemp[line2[3]]=1
            except:
                i+=1          
            

    print(city_gtt_avgtemp)
