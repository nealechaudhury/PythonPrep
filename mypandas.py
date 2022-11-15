import numpy as np
import pandas as pd

def _msg(str=''):
    print ('---'*20)
    print (str)
    print('---' * 20)


if __name__ == '__main__':
    _msg('Load hardcoded data into pandas')
    df = pd.DataFrame (
        # This is the data
        [['Jan',1,2,3,4],
        ['Feb',11,12,13,14],
        ['Mar',21,22,23,24],
        ['Apr',31,32,33,34]],
        index=[0,1,2,3],
        columns=['month','avg high','avg low','record high', 'record low']
    )
    print (df)
    _msg('Open a df file')
    df = pd.read_csv('dataframe_file')
    print (df)



