class Employee:
    _raise = 0.2
    def __init__(self, empFName='', empLName='',salary=10):
        self._empName = empFName + ' ' + empLName
        self._empSalary = salary


    @property
    def get_emp_details(self):
        print ('Name: {0}\nSalary:{1}'.format(self._empName, self._empSalary))

    @property
    def get_emp_raise(self):
        self._empSalary = self._empSalary * (1+self._raise)
        return self._empSalary

    @get_emp_details.setter
    def get_emp_details(self, _newfname, _newlname, _newsalary):
        if _newsalary.isalpha():
            raise ValueError (f'{_newsalary} cannot be alphanumeric please enter float')
        else:
            self._empName = _newfname + ' ' + _newlname
            self._empSalary = _newsalary



class Developer(Employee):
    _raise = 0.5
    def __init__(self, empFName='', empLName='', salary=10):
        super().__init__(empFName, empLName,salary)
        pass
