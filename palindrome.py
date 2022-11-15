import sys

def _checkpalindrome(_str=None):
	if len(_str) %2 != 0:
		_len = int(len(_str) / 2)
		print(_str, _len)
		_left = _str[:_len]
		_right = _str[_len+1:]
		print(_left,_right[::-1], sep='\n')
		if _left == _right[::-1]:
			return True
		else:
			return False
		return False
	else:
		print(_str, len(_str))
		_left = _str[:int(len(_str)/2)]
		_right = _str[int(len(_str)/2):]
		print(_left,_right[::-1], sep='\n')
		if _left == _right[::-1]:
			return True
		else:
			return False

if __name__ == '__main__':
	_str = input().strip()
	print(_checkpalindrome(_str))