'''
You are given  words. Some words may repeat. For each word, output its number of occurrences.
The output order should correspond with the input order of appearance of the word.
See the sample input/output for clarification.
'''
import sys
import collections

def _test(n=None):
	try:
		_n = int(n)
		if _n < 1 or _n > 10E5:
			sys.exit(1)
		return _n
	except ValueError:
		#print(f'{_n} needs to be an integer')
		sys.exit(1)
	else:
		pass


if __name__ == '__main__':
	_n = _test(input().strip())
	#n = _test(_n)
	_l = []
	for i in range(0, _n):
		_l.append(input().strip())
	#print(_l)
	# num of distinct words in the inout
	_counter = collections.Counter(_l)
	# print(_counter)
	#print(_l)
	_s = set()
	_l2 = [x for x in _l if not (x in _s or _s.add(x))]
	#print(_l2)
	print(len(_s))
	_l3 = []
	for i in _counter.keys():
		#print(_counter[i])
		_l3.append(_counter[i])
	print(*_l3)






