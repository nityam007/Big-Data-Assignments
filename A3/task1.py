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
 
'''from pyspark.sql import SparkSession
import sys

spark = SparkSession.builder.appName('A3T1').getOrCreate()

hold = spark.read.csv("C:/Users/Nityam/Dropbox (Old)/My PC (DESKTOP-P3UAN3I)/Downloads/city_sample.csv", sep=',',inferSchema=True, header=True)
df = hold.toPandas()

cities=[]
for i in df.iloc():
    if(i['Country']=='Germany'):
        if(i['City'] not in cities):
            cities.append(i['City'])
            
cities.sort() #Sorting all the cities corresponding to a country in lexiographical order
#print(cities)

avg_temp={} #Stores the City and its average temperature as key-value pairs

for i in cities:
    sum_val=0
    count=0
    for j in df.iloc:
        if (j['City']==i):
            sum_val=sum_val+j['AverageTemperature']
            count+=1
    
    avg_temp[i]=(sum_val/count)

for k in avg_temp:
    count=0
    for p in df.iloc():
        if p['City']==k:
            if(p['AverageTemperature']>avg_temp[k]):
                count+=1
    
    if(count>=1):
        print(k,end="")
        print("\t",end="")
        print(count)  
 '''
