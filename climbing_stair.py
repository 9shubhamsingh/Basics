def climb(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	elif n == 2:
		return 2
	else:
		return climb(n-1) + climb(n-2)



if __name__ == '__main__':
	print('Number of way to reach to the top: {}'.format(climb(24)))
	
