'''Regular methods / Class Methods / Static Methods'''
import sys

class Employee:
	_raise = 1.25
	def __init__(self, fname, lname, basepay):
		self.fname = fname
		self.lname = lname
		self.basepay = basepay

	def getempdetails(self):
		return self.fname, self.lname, self.basepay

	def giveraise(self):
		self.basepay = self.basepay * self._raise

	def printraise(self):
		return self._raise

	@classmethod
	def update_raiseamt(cls, amount):
		cls._raise = amount



if __name__ == '__main__':
	_emp1 = Employee('Ginger', 'Jackson', 1000000)
	_empdetails = _emp1.getempdetails()
	print(_empdetails)
	_emp1.giveraise()
	_newdetails = _emp1.getempdetails()
	print(_newdetails)
	print(_emp1.printraise())
	Employee.update_raiseamt(3)
	_emp1.giveraise()
	_newdetails = _emp1.getempdetails()
	print(_newdetails)
	print(_emp1.printraise())


