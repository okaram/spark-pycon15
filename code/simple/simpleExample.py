# comment out these lines if running from shell 
from pyspark import SparkContext, SparkConf
sc = SparkContext()

# sc represents the Spark Context

rdd1=sc.parallelize( range(1,1000) )
rdd2=rdd1.map(lambda x: x*3) # lazy, notice map is a method
rdd2.reduce(lambda x,y:x+y)
rdd2.filter(lambda x: x%100==0).collect() # collect returns a normal list

# more examples: calculate prime numbers
def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

rdd1=sc.parallelize( range(1,100) ) 
rdd1.filter(isPrime).collect()

# more examples:
rdd1=sc.parallelize( range(1,100) )
rdd1.map(lambda x: x*x).sum()

rdd1.filter(lambda x: x%2==0).take(5)

