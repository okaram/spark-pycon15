class MeanComponent:
	def __init__(self,num):
		self.sum=num;
		self.count=1;
	def selfAdd(self,mc):
		self.sum=self.sum+mc.sum;
		self.count=self.count+mc.count;
		return self;
	def selfAddNum(self,num):
		self.sum=self.sum+num;
		self.count=self.count+1;
		return self;
	def mean(self):
		return self.sum/self.count;
	def __str__(self):
		return "MC: Count={0}, Sum={1}".format(self.count,self.sum)
	def __repr__(self):
		return str(self)
