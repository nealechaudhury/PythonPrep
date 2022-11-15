my_LIST=['Apple', 'Grape', 'Cherry', 'Tomato']
class TestClass:
    def __init__(self, some_val=""):
        self._someval = some_val

    @property
    def GetPassed(self):
        my_val = self._someval
        return my_val
    @staticmethod
    def some_func():
        return 'Hello world'


    @GetPassed.setter
    def GetPassed(self, _newval):
        if _newval not in my_LIST:
            raise ValueError (f'{_newval}  is not in {my_LIST}')
        else:
            self._someval=_newval



if __name__ == "__main__":
    x = TestClass("Test")
    print(x.GetPassed)
