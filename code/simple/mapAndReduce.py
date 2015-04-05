from pyspark import SparkContext

sc = SparkContext()

list1=sc.parallelize( range(1,1000) )

list2=list1.map(lambda x: x*10)
print( 	list2.take(3)	)

theSum=list2.reduce(lambda x,y:x+y)
print(	theSum	)

theSum=list2.sum()
print(	theSum	)

