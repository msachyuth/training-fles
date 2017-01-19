class rectangle:
	
	def __init__(self,l,h):
		self.l=l
		self.h=h
	def area(self):
		return  self.l*self.h
	def perimeter(self):
		return  2*(self.l+self.h)
ob1 = rectangle(2,3);
ob2 = rectangle(4,5);
print ob1.area()
print ob2.perimeter()

