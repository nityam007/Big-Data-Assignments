from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import sys
from functools import reduce
from pyspark.sql.types import *


path1=sys.argv[1]
path2=sys.argv[2]

spark = SparkSession.builder.appName('A3T2').getOrCreate()


df_1=spark.read.option("header","true").csv(path1)
df_2=spark.read.option("header","true").csv(path2)

df_1 = df_1.withColumn("AverageTemperature",df_1.AverageTemperature.cast('float')) 
df_2 = df_2.withColumn("LandAverageTemperature",df_2.LandAverageTemperature.cast('float')) 

df_1=df_1.withColumnRenamed("dt","date")

df_only_join=df_1.join(df_2,df_1.date==df_2.dt)


rdd_1=df_only_join
#rdd_1.show()
#rdd_1.groupBy('date','AverageTemperature','Country').count().show()

#dropDisDF = df.dropDuplicates(["department","salary"])

rdd_3 = rdd_1.groupBy('Country','date').max('AverageTemperature')
#rdd_3.show()

rdd_3=rdd_3.withColumnRenamed("Country","Country_rdd3")
rdd_3=rdd_3.withColumnRenamed("date","date_rdd3")
#rdd_3=rdd_3.withColumnRenamed("City","City_rdd3")
rdd_3=rdd_3.withColumnRenamed("max(AverageTemperature)","max_avg_temp")

#rdd_3=rdd_3.dropDuplicates(['Country_rdd3',"max_avg_temp"])

#rdd_3.show()



rdd_new=rdd_3.join(rdd_1,(rdd_1.date==rdd_3.date_rdd3) & (rdd_1.Country==rdd_3.Country_rdd3) & (rdd_1.AverageTemperature==rdd_3.max_avg_temp) )
rdd_new=rdd_new.dropDuplicates(['Country_rdd3','date_rdd3','max_avg_temp'])

#rdd_new.show()

rdd_new=rdd_new.filter(rdd_new['max_avg_temp'] > rdd_new['LandAverageTemperature'])
#rdd_new.show()
rdd_new=rdd_new.groupBy('Country').count()
rdd_new=rdd_new.orderBy(['Country'])
rdd_new=rdd_new.collect()

#rdd_new=rdd_new.groupBy('date_rdd3','Country').count()
#rdd_new.show()

for i in rdd_new:
    print(i['Country'],end='')
    print("\t",end='')
    print(i['count'])
