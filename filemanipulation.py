'''Open a json file and read it'''
import sys
import json

_jsonfile = r'D:\neale_github\Final_Prep\data\testjson.json'


if __name__ == '__main__':
	# Method 1
	try:
		_f = [i.strip() for i in open(_jsonfile, 'r+')]
	except FileNotFoundError:
		print(f'{_jsonfile} does not exist')
		sys.exit(1)
	else:
		pass
	print(_f)

	# Method 2  But this will have new line characters
	with open(_jsonfile, 'r+') as fh:
		_myl = fh.readlines()
		print(_myl)


	# Method 3
	with open(_jsonfile, 'r+') as fd:
		for l in fd:
			print(l.strip())

