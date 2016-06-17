# Uses python3
import sys

def count(d,coins,n):
	for each in d:
		if n % each == 0 and n-each >= 0:
			coins += 1
			n = n - each
			return (coins,n)

def get_change(n):
	coins = 0    
	d = [10,5, 1]
	while n > 0:
		coins,n = count(d,coins,n)
	return coins

if __name__ == '__main__':
    n = int(sys.stdin.read())
    print(get_change(n))