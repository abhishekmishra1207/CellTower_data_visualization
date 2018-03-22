#pyspark --packages com.databricks:spark-csv_2.10:1.3.0 --master yarn
from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext
import csv

sqlContext = SQLContext(sc)


df = sqlContext.read.format("com.databricks.spark.csv").option("header", "true").load("egypt_usecase.csv")
mapped_data = sqlContext.sql("select lon,lat from df where mcc = 602 ").collect()
fp = open("cell_tower_output.csv", "w")
writer = csv.writer(fp, dialect="excel")
writer.writerows(mapped_data)
fp.close()
