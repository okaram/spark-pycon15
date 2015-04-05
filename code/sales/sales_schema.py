import datetime

class Store:
	def parse(self,line):
		fields=line.split('\t')
		self.id = fields[0]
		self.name = fields[1]
		return self

	def __repr__(self):
		return "Store: id=%s \t name=%s"%(self.id,self.name)


class Product:
	def parse(self,line):
		fields=line.split('\t')
		self.id = fields[0]
		self.name = fields[1]
		self.category=fields[2]
		return self

	def __repr__(self):
		return "Product: id=%s \t name=%s"%(self.id,self.name)


class SaleRow:
	def parse(self,line):
		fields=line.split('\t')
		self.day=fields[0] # maybe parse as date? see below:)
#		self.day=datetime.datetime.strptime(fields[0],"%Y-%m-%d")
		self.store_id=fields[1]
		self.product_id=fields[2]
		self.quantity=int(fields[3]) # let's parse this
		return self

	def __repr__(self):
		return "SaleRow: day=%s \t store_id=%s \t product_id=%s quantity=%d"%(self.day,self.store_id,self.product_id, self.quantity)


