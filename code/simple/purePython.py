# python supports functional programming
a=[1,2,3,4,5]

def add1(x):
	return x+1

map(add1,a) # should return [2,3,4,5,6]

def isOdd(x):
	return x%2==1

filter(isOdd,a) # should return [1,3,5]

def add(x,y):
	return x+y;

reduce(add,a) # should return 15

# now lambdas
(lambda x:x+1) (3) # should return 4

map(lambda x: x+1,[1,2,3]) # should return 2,3,4

# exercises
(lambda x: 2*x) (3)
map(lambda x: 2*x,[1,2,3])
map(lambda t: t[0], [ (1,2), (3,4), (5,6) ])
reduce(lambda x,y:x+y,[1,2,3])
reduce(lambda x,y:x+y,  map(lambda t: t[0], [ (1,2), (3,4), (5,6) ]) )
filter(lambda x: x%2==1, [1,2,3,4,5])

# itertools has chain, which enables us to do flatmap
from itertools import chain

map(lambda t: range(t[0],t[1]) ,[ (1,5), (10,15)])
def flatmap(f,list):
	return chain.from_iterable(map(f,list))
