from pyspark import SparkContext, SparkConf

sc = SparkContext()

simple=sc.parallelize([ ('A',10), ('B',3), ('A',5), ('A',7), ('B',4), ('C',1)])
simple.reduceByKey(lambda x,y: x+y).collect()


# textfile gives us lines, splitting makes tuples
# 'schema' is name | gender | age | favorite language
people=sc.textFile("../../data/people.txt").map(lambda x: x.split('\t'))

# find number of males and number of females
# first get tuples like: ('M',1),('F',1) ... then reduce by key
people.map(lambda t: (t[1],1)).reduceByKey(lambda x,y:x+y).collect()

# now you do number of people per programming language

# let's do youngest person per gender
people.map(lambda t: (t[3],int(t[2]) )).reduceByKey(lambda x,y:min(x,y)).collect()



