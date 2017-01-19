class rectangle:
	def __init__(self,l,h):
		self.l=l
		self.h=h
	def area(self):
		return self.l * self.h
	def perimeter(self):
		return 2*(self.l+self.h)
rect = rectangle(5,7);
print rect.area()
print rect.perimeter()

