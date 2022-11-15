import sys

class Employee:
    _empBump = 0.02


    def __init__(self, *args):
        self._efname=args[0]
        self._elname=args[1]
        self._esalary=args[2]

    @property
    def GetName(self):
        return self._elname + ',' + self._efname

    @property
    def GetSalary(self):
        return self._esalary

    @GetName.setter
    def GetName(self, _new_elname, _new_efname):
       self._efname = _new_efname
       self._elname = _new_elname

    @GetSalary.setter
    def GetSalary(self, _new_salary):
        self._esalary = _new_salary

    def GiveEmpBump(self):
        self._esalary = self._esalary * ( 1+ self._empBump)
        return self._esalary



class Developer(Employee):
    _empBump = 0.05


    def __init__(self, *args):
        super().__init__(*args)




if __name__ == '__main__':
    e = Employee('Emma', 'Slade', 120000)
    print (e.GetName)
    print (e.GetSalary)
    print (e.GiveEmpBump())
    print (f'New salary : {e.GetSalary}')


    d = Developer('Lindsey', 'Slade', 120000)
    print (d.GetName)
    print (d.GetSalary)
    print (d.GiveEmpBump())
    print (f'New Salary : {d.GetSalary}')




