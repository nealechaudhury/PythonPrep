import sys
import getopt


def printList(_myL=[]):
    for v in _myL:
        yield v


if __name__ == '__main__':
    _argL = sys.argv

    for i,v in enumerate(printList(_argL)):
        print(f'{i} -> {v}')



