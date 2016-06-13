# Uses python3
import random

#Inputs
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

def MaxPairwiseProduct(a,n):
	result = 0
	for i in range(0, n):
	    for j in range(i+1, n):
	        if a[i]*a[j] > result:
	            result = a[i]*a[j]	
	return result

def MaxPairwiseProductFast(a,n):	
	max_index1 = -1
	max_index2 = -1

	for i in range(0,n):
		if max_index1 == -1 or a[i] > a[max_index1]:
			max_index1 = i

	for i in range(0,n):
		if (max_index2 == -1 and max_index1 != i) or (a[i] > a[max_index2] and max_index1 != i):
			max_index2 = i



	return a[max_index1]*a[max_index2]

#Final
print MaxPairwiseProductFast(a,n)

# Test Cases
# while(True):
# 	n = random.randint(2,11)
# 	a = []

# 	print(n)
# 	for i in range(0,n):
# 		a.append(random.randint(0,99999))

# 	print(a)
# 	res1 = MaxPairwiseProduct(a,n)
# 	res2 = MaxPairwiseProductFast(a,n)

# 	if res1 != res2:
# 		print('Wrong Answer! %s and %s not equal!' % (res1,res2))
# 		break
# 	else:
# 		print('OK')
