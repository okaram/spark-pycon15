# simple python spark examples, as if they were typed into pyspark, not a full application

# load sales
sales=sc.textFile("sales_*.txt").map(lambda x:x.split('\t'))

#load stores and products
stores=sc.textFile("stores.txt").map(lambda x:x.split('\t'))
products=sc.textFile("products.txt").map(lambda x:x.split('\t'))

# calculate sales by day
sales_by_day=sales.map(lambda x : (x[0],int(x[3])) ).reduceByKey(lambda x,y:x+y)

#store sales by day
sales_by_day.map(lambda l: "{0}\t{1}".format(l[0],l[1])).saveAsTextFile("sales_by_day")

