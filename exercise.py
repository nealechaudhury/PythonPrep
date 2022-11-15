import os

if __name__ == '__main__':
	_l = (input().strip()).split()
	print(_l)
	_s = [int(i) for i in _l]
	_sum = (sum(i) for i in _s)
	_sum = 0
	for v in _s:
		_sum += v
	print(f'Summed items in list = {_sum}')
	_summedlist = list(map(sum, _s))
	print(_summedlist)