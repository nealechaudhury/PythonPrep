#from contextlib import contextmanager


class ManageFile:
    def __init__(self, _f):
        self._myfile = _f

    @property
    def File(self):
        _myF=self._myfile
        return _myF

    @File.setter
    def File(self, _newf):
            self._myfile = _newf

    # @property
    # @contextmanager
    # def TestFile(self):
    #     print (f'File to open is -> {self._myfile}')
    #     try :
    #         f = open(self._myfile, 'r+')
    #         yield f
    #     except FileNotFoundError as err:
    #         print (err)
    def __enter__(self):
        self._file=open(self._myfile,'r+')
        return self._file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._file:
            self._file.close()


def _printL(_l=[]):
    for i in _l:
        yield i.strip()



if __name__ == '__main__':
    f = ManageFile('val.txt')
    print(f'File to be opened : {f.File}')
    with f as fh:
        _myl = fh.readlines()

    for i, v in enumerate(_printL(_myl)):
         print (f'{i} -> {v}')

    # with f.TestFile as fh:
    #     print(fh, type(fh))
    #
    #
    # with open('val.txt', 'r+') as fh:
    #     _myl= fh.readlines()
    #
    # for i, v in enumerate(_printL(_myl)):
    #     print (f'{i} -> {v}')








