'getter setter delete - decorators in a class'

class Employee:
	def __init__(self, fname, lname):
		self.fname = fname
		self.lname = lname

	def getEmployee(self):
		return self.fname, self.lname

	@property
	def getemail(self):
		return self.fname + '.' + self.lname + '@bluehorseshoe.com'

	@getemail.setter
	def getemail(self, name):
		self.fname = name.split()[0].strip()
		self.lname = name.split()[1].strip()
		return self.fname + '.' + self.lname + '@bluehorseshoe.com'



if __name__ == '__main__':
	emp1 = Employee('Ginger', 'Jackson')
	print(emp1.getEmployee())
	print(emp1.getemail)
	emp1.getemail = 'Ginger Chaudhury'
	print(emp1.getemail)
	print(emp1.getEmployee())
