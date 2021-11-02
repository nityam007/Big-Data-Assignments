from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import sys
from functools import reduce
from pyspark.sql.types import *

country=sys.argv[1]
path=sys.argv[2]

spark = SparkSession.builder.appName('A3T2').getOrCreate()



df=spark.read.option("header","true").csv(path)

df_only_country=df.where(df.Country==country)

df2= df_only_country.withColumn("AverageTemperature",col("AverageTemperature").cast(FloatType()))

df3=df2.groupBy("City").mean("AverageTemperature")

oldColumns = df3.schema.names

newColumns=["ew","cityavgtemp"]

temp= reduce(lambda df3, idx: df3.withColumnRenamed(oldColumns[idx], newColumns[idx]), range(len(oldColumns)), df3)

joined_df=df2.join(temp,df2.City==temp.ew)

final_res=joined_df.filter(joined_df.AverageTemperature>joined_df.cityavgtemp).groupBy("City").count()

final_res=final_res.orderBy(['City'])

rdd_final_vals=final_res.collect()

for i in rdd_final_vals:
    print(i['City'],end="")
    print("\t",end="")
    print(i['count'])
