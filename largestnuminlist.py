import os

if __name__ == '__main__':
	_l = [int(i) for i in (input().strip()).split()]
	print(sorted(_l, reverse=True)[0])
