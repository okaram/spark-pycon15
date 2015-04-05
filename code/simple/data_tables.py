# data tables have explicit schemas, and a potentially better query optimizer
from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext

sc = SparkContext()
sqlCtx = SQLContext(sc)

# you can read from json files (one object in each line, need quotes around field names)
# you get a datatable which is a kind of RDD, with schema info, and each tuple is of class Row
people=sqlCtx.jsonFile("../../data/people1.json")

# the show method is similar to collect, but displays nicely
people.show()

# the select method is almost-equivalent to map
# can use strings, or columns from datatable in expressions
people.select("name",people.age+1).show()

# can use filter (same as in rdd)
people.filter(people.age>30)

# can use [] instead of filter, like in pandas
people[people.gender=='F']

# can use groupBy, and then count() or a few other operators
people.groupBy(people.gender).count()

# can use sql ! 

#first register as temp table
people.registerTempTable("people")

sqlCtx.sql("select name, age FROM people").show()

sqlCtx.sql("select gender,avg(age) AS AvgAge FROM people GROUP BY gender").show()

