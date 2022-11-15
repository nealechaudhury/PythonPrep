def print_vals(_list):
    for v in _list:
        yield (v)




if __name__ == '__main__':
    _myl=['Fauda', ' Cas de Papal', 'Peaky Blinders', 'Hannibal']

    for i,v in enumerate(print_vals(_myl)):
        print (f'{i} -> {v}')


