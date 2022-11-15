import os
import sys
import collections


def _nineteen(_l=None):
	'''
	Write a Python program find a list of integers with
	exactly two occurrences of nineteen and at least three occurrences of five
	'''
	_cnt = collections.Counter(_l)
	if _cnt[19] == 2 and _cnt[5] >=3:
		return True
	else:
		return False

def _saidlist(_l=None):
	'''
	Write a Python program that accept a list of integers and check the length and the fifth element.
	Return true if the length of the list is 8 and fifth element occurs thrice in the said list
	'''
	if len(_l) == 8 and collections.Counter(_l)[_l[5]] == 3:
		return True
	else:
		return False

def _stonepiles(_n=None):
	'''
	We are making n stone piles! The first pile has n stones.
	If n is even, then all piles have an even number of stones.
	If n is odd, all piles have an odd number of stones. Each pile must more
	stones than the previous pile but as few as possible.
	Write a Python program to find the number of stones in each pile.
	'''
	try:
		_int = int(_n)
		print(_int)
		#_l = [i for i in range(_int,_int*2+1,2)]
		_l=[]
		_count = _int
		for val in range(0, _int):
			#print(val, _count)
			_l.append(_count)
			#_l[val] = _count
			_count += 2
		print(_l)
	except ValueError:
		print(f'{_n} needs to be an integer')
	else:
		pass


def _substr(_l=None):
	print(len(_l))
	_ret = ''
	for e,i in enumerate(_l):
		print(e)
		if e < len(_l)-1:
			if _l[e] in _l[e+1]:
				_ret = "TRUE"
			else:
				_ret = "FALSE"
	return _ret

def _checkstr(str1=None):
	return str1[len(str1)-2] in str1[len(str1)-1] and str1[len(str1)-2] != str1[len(str1)-1]

def _differby(_l=None, val=None):
	try :
		_val = int(val)
		_l = [int(i[e]) - int(i[e+1]) for e,i in enumerate(_l)]
	except ValueError:
		print(f'{val} should be an integer')
	else:
		pass


def _rank (_l=None, rank=None):
	'''Get the nth max value'''
	try:
		_rank = int(rank)
		_count = collections.Counter(_l)
		print(_count.keys())
		print(f'Max value is {max(_l)}')
		print(f'Min value is {min(_l)}')
		print(_l)
		_s = set(_l)
		print(_s)
		_l2 = sorted(list(_s))
		print(_l2)
		print(f'{_rank} highest = {_l2[len(_l2) - _rank]}')

	except ValueError:
		print(f'Error : {rank} needs to be an integer - script aborting')
	else:
		pass





if __name__ == '__main__':
	'''
	_l = [int(i) for i in (input().strip()).split()]
	if _nineteen(_l):
		print(f'BINGO {_l} has 2 19s and 3 5s')
	else:
		print('FALSE')
	_l = [int(i) for i in (input().strip()).split()]
	print(_saidlist(_l))
	_stonepiles(input().strip())
	print(_substr(list((input().strip()).split())))
	print(_checkstr(input().strip()))
	'''
	try:
		_l = [int(i) for i in (input().strip()).split()]
	except ValueError:
		print('Contents of listneed to be integer')
		sys.exit(1)
	else:
		pass
	_r = input().strip()
	#print(_l, sum(_l), _rank(_l, _r) )
	_rank(_l, _r)





