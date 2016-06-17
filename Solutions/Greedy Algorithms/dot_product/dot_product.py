#Uses python3

import sys

def min_dot_product(a, b):
    #Take the Max of a, multiply by the minimum of b. 
    res = 0
    for i in range(len(a)):    
        i = a.index(max(a))
        ii = b.index(min(b))
        res += a[i]*b[ii]
        a.remove(a[i])
        b.remove(b[ii])
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(min_dot_product(a, b))
    
