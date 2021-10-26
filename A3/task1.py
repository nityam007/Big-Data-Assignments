import csv


country='India'
path='/Users/Darshilshah/Downloads/city_sample_5percent.csv'
city_vs_avgtemp=dict()
city_count=dict()
file=open(path,"r")
data=file.read()
i=0
with open(path) as csv_file:

    csv_reader=csv.reader(csv_file)

    for line in csv_reader:
        if(line[4]==country):
            
            if(line[3] in city_count):
                try:
                    city_count[line[3]]+=float(line[1])
                except:
                    #print(line)
                    i+=1
                
            
            else:
                try:
                    city_count[line[3]]=float(line[1])
                except:
                    #print(line)
                    i+=1
                
    for x in city_count:
         occurences=data.count(x)
         city_count[x]=city_count[x]/occurences
    print(city_count)

print(i)
