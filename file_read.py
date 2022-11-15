import sys

class FileHandler:
    def __init__(self, fname_passed):
        self._fname = fname_passed


    @property
    def get_fname(self):
        try:
            open (self._fname, 'r+')
        except FileNotFoundError as e:
            print (f'{e}')
        finally:
            return(self._fname)


    @get_fname.setter
    def get_fname(self, _newfname):
        self._fname = _newfname

    @staticmethod
    def sep(msg = 'blah'):
        print ('{0}\n{1}\n{2}'.format('--'*20, msg, '--'*20))

    @staticmethod
    def PrintL(_l=[]):
        for v in _l:
            yield v.strip()

    def readFile(self):
        _file = self._fname
        FileHandler.sep('Method 1: Open ' + _file + ' and read directly from it')
        fh = open(_file, 'r+')
        _myL = fh.readlines()
        fh.close()
        for i,v in enumerate(FileHandler.PrintL(_myL)):
            print (f'{i} -> {v}')

        FileHandler.sep('Method 2: Open ' + _file + ' using list comprehension - good way')
        _mylines = [line.strip() for line in open(_file, 'r+' ,encoding='utf-8')]
        for i,v in enumerate(FileHandler.PrintL(_mylines)):
            print (f'{i} -> {v}')

        FileHandler.sep('Method 3: list comprehension')
        with open (_file, 'r+') as fh:
            _myL = fh.readlines()

        if not fh.closed :
            print (f'{_file} is still open')

        for i,v in enumerate(FileHandler.PrintL(_myL)):
            print (f'{i} -> {v}')





if __name__ == '__main__':
    fh = FileHandler('test.txt')
    fh.get_fname
    fh.readFile()
