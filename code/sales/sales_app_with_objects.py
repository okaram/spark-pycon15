from pyspark import SparkContext, SparkConf
import sys
import sales_schema

appName="salesApp"
master="local"
conf = SparkConf().setAppName(appName)
sc = SparkContext(conf=conf)

base_path="../../data/sales/"
output_path=sys.argv[1]

#load stores,products,sales
stores=sc.textFile(base_path+"stores*.txt").map(lambda x:sales_schema.Store().parse(x))
products=sc.textFile(base_path+"products.txt").map(lambda x:sales_schema.Product().parse(x)) # id | name | category

sales=sc.textFile(base_path+"sales_*.txt").map(lambda x:sales_schema.SaleRow().parse(x))

# calculate and store sales by day
sales_by_day=sales.map(lambda x : (x.day,x.quantity)).reduceByKey(lambda x,y:x+y)
#save sales by day
sales_by_day.map(lambda l: "{0}\t{1}".format(l[0],l[1])).saveAsTextFile(output_path+"sales_by_day")

#calculate sales by store
sales_by_store=sales.map(lambda x : (x.store_id,x.quantity) ).reduceByKey(lambda x,y:x+y)

#now join with stores to get store names
sales_by_store_joined=sales_by_store.join(stores.map(lambda x: (x.id,x.name))) # output is: store_id | <qty | store>

#reshape
sales_by_store_with_name=sales_by_store_joined.map(lambda x: (x[1][1], x[1][0]))

# and save
sales_by_store_with_name.map(lambda l: "{0}\t{1}".format(l[0],l[1])).saveAsTextFile(output_path+"sales_by_store")


