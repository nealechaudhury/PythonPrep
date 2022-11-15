import os

def strfunc(s):
	print(f'String : {_s}')
	print(f'Length : {len(_s)}')
	print(f'First value : {_s[0]}')
	print(f'Except the last value : {_s[:-1]}')
	print(f'Second to 4th values : {_s[2:4]}')
	print(f'Everything except first value : {_s[1:]}')
	print(f'All values except first and last : {_s[1:-1]}')


def _list(_s):
	# _l = list(_s)
	print(_s)
	print(_s[-1])  # Last item of the list
	print(_s[-2])  # Second to last item of the list
	print(_s[1:4]) # Print element 1 thru 3
	print(_s[2:]) # Print element 2 thru end
	### X[I:J]  Means give everything from Ith element upto (not including J'th element
	print(_s[:4])## Everything from start to 3rd element
	print(_s[:-1]) # Everything but the last element
	print(_s[::-2]) #Every 2nd element in reverse order
	print(_s[::-1]) #Print list in reverse order
	print(_s[:5:-1]) #Start from end and write until the 5th element
	#_s[2]=8 # Wont work bc this is a str
	_l = list(_s)
	print(_s, _l)
	_l[2] = 'aaa'
	print(_s, _l)




if __name__ == '__main__':
	_s = input().strip()
	#strfunc(_s)
	_list(_s)