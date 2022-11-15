class myFileClass:
    def __init__(self, fname):
        self._fname = fname
        ## Check if issues with the file
        try:
            open(self._fname, 'r+')
        except FileNotFoundError as e:
            print(e)
        finally:
            pass

    ## getter
    @property
    def fname(self):
        return self._fname

    @staticmethod
    def sep(msg):
        print (f'{"--"*20}\n{msg}\n{"--"*20}')


    def readfname(self):
        my_f = self._fname
        myFileClass.sep('Open File way 1 :')
        fh = open(my_f, 'r+')
        print (f'{fh.read()}')
        fh.close()

        myFileClass.sep('Second way to use context manager - readlines will output to a list')
        with open(my_f, 'r+') as fh:
            myl2=fh.readlines()
            #print (f'{fh.readlines()}') # readlines will write to a list
            print (f'{myl2}') # readlines will write to a list

        myFileClass.sep('Third way of using similar context manager - readline will read one line at a time')
        with open(my_f, 'r+') as fh:
            print (f'{fh.readline()}')
            print (f'{fh.readline()}')

        myFileClass.sep('Fourth way context manager ')
        with open(my_f, 'r+') as fh:
            myv = fh.read()
            print (f'{myv} -> {type(myv)}')

        print (fh.closed)
        myFileClass.sep('Fifth way using list comprehension')
        lines = [line.strip() for line in open(_fname, 'r+')]

        print (fh.closed)
        print (lines)



if __name__ == '__main__':
    _fname = 'D:\\neale_github\\Misc\\my_file.txt'
    f = myFileClass(_fname)
    print(f'File passed : {f.fname}')
    f.readfname()

