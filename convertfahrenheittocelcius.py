import os

def _converttocelcius(_F=None):
	_C = (_F-32)*100/180
	return _C

if __name__ == '__main__':
	_F = float(input().strip())
	try:
		_val = _converttocelcius(_F)
	except ValueError:
		print(f'{_F} is not a float')
	else:
		print(f'{_F} Fahrenheit = {_val} Celcius')