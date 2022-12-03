import sys
import collections


def _test1(val=None):
	return True if 3 < len(val) <= 10E4 else False

def _test2(val=None):
	return True if len(dict(collections.Counter(val))) > 3 else False


def _check(val=None):
	_a = _test1(val)
	_b = _test2(val)
	assert (_a, _b) == (True, True)



if __name__ == '__main__':
	'''
	Check input constraing that 
	1.  3 < S <= 10E4
	2.  There are atleast 3 distinct characters in the name
	So here lets use assert and return to the try block
	'''
	try:
		_companyname = input().strip()
		_check(_companyname)
	except AssertionError:
		print('Please enter name of company greater than 3 characters\nand having more than 3 + distinct characters')
		sys.exit(1)

	print(f'All good company added ->  {_companyname}')






	# try:
	# 	_companyname = input().strip()
	# 	#_checkinput_range(_companyname)
	# 	_test(_companyname)
	# except AssertionError as error:
	# 	print('Company name needs to be in the range of 3 and 10E4')
	# 	sys.exit(1)
	#
	# _strdict = dict(collections.Counter(_companyname))
	# print(_strdict)
	# _sval = [_n for _n in set([i for i in _strdict.values()])]
	# _sval.sort(reverse=True)
	# # print(_sval, len(_sval))
	# _sval2 = _sval[:3]
	# print(_sval2)
	# _commonstrings = [k for k, v in _strdict.items() if v in _sval2]
	# print(_commonstrings)
