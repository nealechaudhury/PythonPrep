import os
from contextlib import contextmanager

# Use as decorator
@contextmanager
def _open_f(_fname='', _mode = 'r+'):
    try:
        _f = open ( _fname, _mode )
        yield _f
        #_f.close()
    finally:
        _f.close()


def _printl(_l=''):
    for v in _l:
        yield v.strip()


@contextmanager
def _gotodir(_newdir=''):
    _cwd=os.getcwd()
    try:
        os.chdir(_newdir)
        yield
    finally:
        os.chdir(_cwd)

if __name__ == '__main__':
    _f = 'val.txt'
    _m = 'r+'
    with _open_f(_f, _m) as fh:
        _l=fh.readlines()

    for i, v in enumerate(_printl(_l)):
        print(f'{i} -> {v}')

    print(fh.closed)

    ## Example 2 go from cwd to a new directory
    # _cwd=os.getcwd()
    # print (_cwd)
    # os.chdir('d:\\neale_github')
    # _cwd=os.getcwd()
    # print(_cwd)
    ## Using context manager:
    print(f'Current dir : {os.getcwd()}')
    with _gotodir('d:\\neale_github') as _n:
        print (f'New dir : {os.getcwd()}')


    print (f'Outside - we should be back to old cwd : {os.getcwd()}')
