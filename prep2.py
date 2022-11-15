import sys



if __name__ == '__main__':
	# _nm = [i for i in (input().strip()).split(',')]
	_nmstr = [i for i in input().strip().split(',')]
	print(_nmstr)
	print(f'Sorting by first name \n{sorted(_nmstr)}')
	## Sort by last name
	## Flip the names so create a list that will have last name, middle name, first name
	_l2 = []
	for i in _nmstr:
		# print(i)
		# print(i.split(' ')[::-1])
		_str = i.split(' ')[::-1]
		_str = ' '.join(_str)
		# print(_str)
		_l2.append(_str)
	#print(_l2)
	_l3 = sorted(_l2)
	_l4 = []
	for i in _l3:
		#print(i)
		_str = ' '.join(i.split()[::-1])
		#print(_str)
		_l4.append(_str)
	print(f'Sorted by last name \n{_l4}')



