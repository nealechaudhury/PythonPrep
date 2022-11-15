import sys
import json
import pandas

_jsonfile = r'D:\neale_github\Final_Prep\data\testjson.json'


if __name__ == '__main__':
	# Key to load json data
	# use with
	with open(_jsonfile, 'r+') as fd:
		_jsondata = json.load(fd)

	print(type(_jsondata),_jsondata)
	for k, v in _jsondata.items():
		print(k,v)

	for t in _jsondata['topping']:
		print(t,t['id'],t['type'])