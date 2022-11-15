def _sq(x=0):
    return x*x



if __name__ == '__main__':
    print (_sq)
    f = _sq(5)
    g = _sq
    print(f'For 2 -> {_sq(2)} \n{f}')
    print(f'{g} -> {g(5)}')