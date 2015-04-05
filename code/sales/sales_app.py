from pyspark import SparkContext, SparkConf
import sys
appName="salesApp"
master="local"
conf = SparkConf().setAppName(appName)#.setMaster(master)
sc = SparkContext(conf=conf)

base_path="../../data/sales/"
output_path=sys.argv[1]#"/home/curri/projects/spark/out/"
# load sales
sales=sc.textFile(base_path+"sales_*.txt").map(lambda x:x.split('\t')) # Day | Store | Product | Qty

#load stores and products
stores=sc.textFile(base_path+"stores.txt").map(lambda x:x.split('\t')) # id | name
products=sc.textFile(base_path+"products.txt").map(lambda x:x.split('\t')) # id | name | category

# calculate sales by day
sales_by_day=sales.map(lambda x : (x[0],int(x[3])) ).reduceByKey(lambda x,y:x+y)

#save sales by day
sales_by_day.map(lambda l: "{0}\t{1}".format(l[0],l[1])).saveAsTextFile(output_path+"sales_by_day")

#calculate sales by store
sales_by_store=sales.map(lambda x : (x[2],int(x[3])) ).reduceByKey(lambda x,y:x+y)

#now join with stores to get store names
sales_by_store_joined=sales_by_store.join(stores) # output is: store_id | <qty | name>

#reshape
sales_by_store_with_name=sales_by_store_joined.map(lambda x: (x[1][1], x[1][0]))

# and save
sales_by_store_with_name.map(lambda l: "{0}\t{1}".format(l[0],l[1])).saveAsTextFile(output_path+"sales_by_store")






