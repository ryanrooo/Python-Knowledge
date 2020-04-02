import pyspark
from pyspark.sql import SparkSession, Row
sc = SparkSession.builder.master("local[*]").getOrCreate()
import pandas as pd
from hdfs3 import HDFileSystem
hdfs = HDFileSystem(host='horton')
hdfsS = HDFileSystem(host='stampy')

data = sc.read.csv('/user/rynguyen/state_info.csv') #Doesnt include header

data.show() # shows headers as _c0 , _c01 because header is not = True

data.printSchema() # prints column settings"

data.select("_c0").show()
data.registerTempTable("Data")

sc.sql("Select * from Data where _c0 = 'California'").show()

# Optimal way of reading data files into data frame
df = sc.read.format('csv').options(header='true', inferSchema='true').load('/user/rynguyen/state_info.csv')
df.show() # includes headers


df.createOrReplaceTempView("data") # Returns results as data frame"

Houseseats2 = sc.sql("select * from data where HouseSeats = 2").show() #data frame query"

df.createGlobalTempView("data") #Temporary view that is shared among all sessions and keep alive until the Spark application terminates"

frame1 = sc.sql("Select * from global_temp.data where HouseSeats = 2").show()

df.select("State").show() #Untyped Dataset Operations (aka DataFrame Operations)"

df.select(df["Capital"], df["State"]).show()

df.groupby("HouseSeats").count().show()


scdata = sc.read.format('csv').options(header='true', inferSchema='true').load('/user/rynguyen/cogsley_clients.csv')
scdata.show()

summ = scdata.describe("Summary Quote").show()

summ = scdata.describe("Summary Quote").show() #Can only save if the code doesn't contain \".show()\"\""

save = summ.write.save("sum.csv", format="csv")

scdata.columns

frame2 = scdata.filter((scdata.MarketCapAmount > 1990000000) & (scdata.IPOyear > 2004))

save2 = frame2.write.save("ex.csv", format="csv")
