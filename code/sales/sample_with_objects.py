import sales_schema

base_path="../../data/sales/"
stores=sc.textFile(base_path+"stores*.txt").map(lambda x:sales_schema.Store().parse(x))

sales=sc.textFile(base_path+"sales_*.txt").map(lambda x:sales_schema.SaleRow().parse(x))

