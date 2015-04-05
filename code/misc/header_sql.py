from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext

sc = SparkContext()
sqlCtx = SQLContext(sc)

