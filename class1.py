import sys

class Shape:
	def __init__ (self, passedcolor=None, numsides=None):
		# This is the constructor where u initialize the method calling the factory (class)
		self.color = passedcolor
		self.numsides = numsides

	def get_Shape(self):
		return self.color, self.numsides

	def change_Shape(self, newcolor=None, numsides=None):
		self.color = newcolor
		self.numsides = numsides


class Rectangle(Shape):
	def __init__(self, color, numsides, length, width):
		super().__init__(color, numsides)
		self.length = length
		self.width = width

	def getRectangle(self):
		return self.color, self.numsides, self.length, self.width

	def getArea(self):
		return self.length * self.width

	def updatedims(self, newlength, newwidth):
		self.length = newlength
		self.width = newwidth


if __name__ == '__main__':
	_shape = Shape('RED', 4)
	_color, _numsides = _shape.get_Shape()
	print(f'Obj1[Color passed] : {_color}\nObj1[Num sides] : {_numsides}')
	_rect = Rectangle('blue', 5, 10,4)
	print(_rect.get_Shape())
	print(_rect.getRectangle())
	print (f'Area is {_rect.getArea()}')
	## Now change shape using methods in Rectangle class
	_rect.change_Shape('GREEN', 5)
	print(_rect.get_Shape())
	print(_rect.getRectangle())
	## get all methods of Shape class
	print(Shape.__dict__)
	## Change length and width and redo area
	print(f'Original Area : {_rect.getArea()}')
	_rect.updatedims(9,3)
	print(f'New Area : {_rect.getArea()}')

