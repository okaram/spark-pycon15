# data tables have explicit schemas, and a potentially better query optimizer
from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext

sc = SparkContext()
sqlCtx = SQLContext(sc)

# can also add schema to already-existing tuples
from pyspark.sql import *
from pyspark.sql.types import *

base_path="../../data/sales/"
# load sales
sales_rdd=sc.textFile(base_path+"sales_*.txt").map(lambda x:x.split('\t')).map(lambda t: (t[0],t[1],t[2],int(t[3]))) # Day | Store | Product | Qty
sales_fields=[
	StructField('day',StringType(),False), # name,type,nullable
	StructField('store',StringType(),False), 
	StructField('product',StringType(),False), 
	StructField('quantity',IntegerType(),False), 
]
sales_schema=StructType(sales_fields)
sales=sqlCtx.createDataFrame(sales_rdd,sales_schema)

#load stores ... I'm lazy and use string ids
stores_rdd=sc.textFile(base_path+"stores.txt").map(lambda x:x.split('\t')) # id | name
stores_fields=[
	StructField('id',StringType(),False), # name,type,nullable
	StructField('name',StringType(),False), 
]
stores=sqlCtx.createDataFrame(stores_rdd,StructType(stores_fields))

products_rdd=sc.textFile(base_path+"products.txt").map(lambda x:x.split('\t')) # id | name | category
products_fields=[
	StructField('id',StringType(),False), # name,type,nullable
	StructField('name',StringType(),False), 
	StructField('category',StringType(),True), 
]
products=sqlCtx.createDataFrame(products_rdd,StructType(products_fields))

sqlCtx.registerDataFrameAsTable(sales,"sales")
sqlCtx.registerDataFrameAsTable(stores,"stores")
sqlCtx.registerDataFrameAsTable(products,"products")

# can do SQL, including joins and GroupBy !!
sqlCtx.sql("SELECT * FROM sales sa join stores st on sa.store=st.id").show()
sqlCtx.sql("SELECT * FROM sales s join products p on s.product=p.id").show()

# .explain
# .agg
from pyspark.sql import functions as funcs

sales.groupBy('day').agg(funcs.min('store').alias('MinStore'),funcs.max('quantity').alias('MaxQty')).show()
