class ClassName:
	def __init__(self,a):
		self.a = a
		print "object created"
	def __str__(self):
		return str(self.a)
	def __del__(self):
		print"object removed"
obj = ClassName(10);
print obj
del obj


