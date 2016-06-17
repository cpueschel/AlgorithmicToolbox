# Uses python3
import sys

def optimal_summands(n):
    summands = []
    #Intialize Variables
    k = n
    l = 1
    while k >= l:
        if k <= 2*l:
            summands.append(k)
        else:
            summands.append(l)
        k = k-l
        l = l+1
    return summands

# print(optimal_summands(8))
if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
