import calendar
import datetime
import os
from subprocess import call


def mysep(msg=None):
    print (f'{"---"*20}\n{msg}\n{"---"*20}')


def _is(_str=None):
    _append = ""
    print (f'-----> {_str} and {_str[:2:]}')
    if not (_str[:2] == "is"):
        _append="is"
        print (f'-----> {_str} need to append {_append}')
    return _append+_str


if __name__ == '__main__':
    ''' 
    mysep('Flip a list of input strings')
    my_name = input("Please enter name :")
    my_l=my_name.split()
    print(my_l[-1::-1])
    print(f'\nNow reverse the strings and print them out\n')

    for e,v in enumerate(my_l[-1::-1]):
        print(f'{e} -> {v}')
        new_l=(v)[-1::-1]
        print (new_l)
    mysep('Accept a csv list from user and generate a list and tuple')
    user_val=input('Please enter a list of csv values')
    myl=list(user_val.split(','))
    myt=tuple(user_val.split(','))

    for e, v in enumerate(myl):
        print (f'{e} --> {v} --> {type(myl)}')

    print (f'{myt} -> {type(myt)}')
    
    mysep('Accept a file name from an user and print the extension of the file name')
    myf=input('Please enter the file name: ')
    print (f'Extension of {myf} is {myf.split(".")[-1::]}')

    mysep('Convert exam date of 11 , 12 , 2014 to 11/12/2014')
    mydt =input('Please enter date e.g. 11, 12 , 2014')
    mydt2=" / ".join(mydt.split(","))
    print(f'{mydt} -> {mydt2}')
    
    mysep('Write a pythonprogram that takes a number and gives n+nn+nnn')
    mynum = input('Please enter a number :')
    if not mynum.isdigit():
        raise ValueError (f'{mynum} is not a number ')


    print(f'Entered value : {mynum} Adding 4 to it {int(mynum) + 4}')
    mystr  =int(str(mynum)*2)
    mystr2 =int (str(mynum)*3)
    print(f'So need to do : {mynum} + {mystr} + {mystr2}')
    print (f'{mystr} -> {type(mystr)}')
    print (f'{mystr2} -> {type(mystr2)}')
    _newvalue = int(mynum) + int(mystr) + int(mystr2)
    print(_newvalue)
    mysep('Write a python program that prints calendar of given month and year')
    print (calendar.month(theyear=2020, themonth=4,w=0,l=0))

    mysep('Number of days between two dates ')
    mydt1 = input('Please enter the first date - YYYY,M,D : ')
    mydt2 = input('Please enter the first date - YYYY,M,D : ')

    #print (f'{mydt1} , {type(mydt1)}\n{mydt2} , {type(mydt2)}')

    _numdays = datetime.date(int(mydt1.split(',')[0]), int(mydt1.split(',')[1]), int(mydt1.split(',')[2])) - datetime.date(int(mydt2.split(',')[0]), int(mydt2.split(',')[1]), int(mydt2.split(',')[2]))
    print(f'{_numdays.days} number of days')
    mysep ('if string starts with is then dont change else add is')
    mystr1 = 'isAlpha'
    mystr2 = 'Alphawithoutis'
    print (_is(mystr1))
    print (_is(mystr2))
   
    '---------- Good snip below ----------- 
    mysep('Write a program to check if input is a vowel or not')
    _vowel="aeiou"
    _vl=(',').join(_vowel).split(',')
    print (f'{_vl} and {type(_vl)}')
    _v=input('Please enter an alphabet :')
    if (_v in _vl):
        print (f'{_v} is a vowel.')
    
    mysep('Check if file exists')
    _fname='D:\\neale_github\\Misc\\my_file.txt'
    print (os.path.isfile(_fname))
    '''
    mysep('Run a dir command')
    call('dir')



