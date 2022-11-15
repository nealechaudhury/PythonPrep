import sys
import random

NFLIX_SHOWS = ['Fauda', ' Cas de Papal', 'Peaky Blinders', 'Hannibal']

class Nflix:
    def __init__(self, _showname='Some Val'):
        self._show = _showname

    _list_inside_class = [
        'Song 1',
        'Song 2',
        'Song 3'
    ]

    @property
    def PrintShow(self):
        _myshow = self._show
        return (_myshow)

    @PrintShow.setter
    def PrintShow(self,_newVal):
        if _newVal not in NFLIX_SHOWS:
            raise ValueError (f'{_newVal} is not part of our list')
        self._show=_newVal

    @staticmethod
    def _test(someval = 'blah'):
        print (f'Val passed is {someval}')

    @classmethod
    def _getsong(cls):
        return (cls._list_inside_class)





























'''



class ShowNewName:
    def __init__(self, val_passed = 'test'):
        self._myval = val_passed

    @property
    def MyShow(self):
        return(self._myval)

    # Set the name of the show instead of passing it as a class variable
    @MyShow.setter
    def MyShow(self, _newVal):
        self._myval = _newVal


def print_nflix_shows():
    for i,v in enumerate(NFLIX_SHOWS):
        print (f'{i} -> {v}')


if __name__ == '__main__':
    print ('{0}'.format(sys.version))
    print (f'{sys.version}')
    print('Get a random value from the list')
    print(random.choice(NFLIX_SHOWS))




'''
