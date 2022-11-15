import sys


if __name__ == '__main__':
    _myval = input('Please enter a date YYYY,MM,DD :')
    print (f'{_myval}')
    _myL = _myval.split(',')
    print (f'List : {_myL} Type : {type(_myL)}\nString : {_myval}, Type : {type(_myval)}')
    print (f'{_myL[0]}')

