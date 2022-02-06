"""
Generating Subset
"""
subset = []

def gen_sub(n:int,k:int):
	#Base Case
	if k == n+1:
		print(subset)

	#Choice
	else:
		subset.append(k)
		gen_sub(n,k+1)
		subset.pop()
		gen_sub(n,k+1)

if __name__ == '__main__':
	n = 3
	gen_sub(n,1)



