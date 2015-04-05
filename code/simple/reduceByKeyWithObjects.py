# remember to call with --py-files person.py to include this one
from person import Person


from pyspark import SparkContext, SparkConf

sc = SparkContext()

# textfile gives us lines, now we call Person's parse method
people=sc.textFile("../../data/people.txt").map(Person().parse)

# find number of males and number of females
# first get tuples like: ('M',1),('F',1) ... then reduce by key
people.map(lambda t: (t.gender,1)).reduceByKey(lambda x,y:x+y).collect()

# now you do number of people per programming language

# let's do youngest person per gender
people.map(lambda t: (t.gender,t.age )).reduceByKey(lambda x,y:min(x,y)).collect()



