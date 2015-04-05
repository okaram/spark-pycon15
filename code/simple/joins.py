from pyspark import SparkContext

sc = SparkContext()

states=[
	("AL","Alabama"),
	("AK","Alaska"),
	("AR","Arizona")
]; # apologies to the other 47 ...

populations=[
	("AL",4779736),
	("AK",710231),
	("AR",6392017)
]; # according to 2010 census, from Wikipedia

states_rdd=sc.parallelize(states)
populations_rdd=sc.parallelize(populations)

print(	states_rdd.join(populations_rdd).first()	);	

