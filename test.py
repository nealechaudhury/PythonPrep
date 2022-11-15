import re

def divide_chunks(l, n):
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]


if __name__ == '__main__':
    _n = int(input().strip())
    _l = []
    for i in range(0, _n):
        _l.append(re.split(r'\t',input().strip()))
    print(_l)
    _encoded = input().strip()
    _e = []
    for i in range(0, len(_encoded), 6):
        _e.append(_encoded[i:i+chunk_size])

    print(_e)
    _dict = {}
    for i in _l:
        _dict[int(i[1])] = i[0]

    print(_dict)