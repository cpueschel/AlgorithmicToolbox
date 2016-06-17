# Uses python3
import sys
from operator import truediv

def get_optimal_value(capacity, weights, values):
        V = 0.000
        W = capacity
        for i in range(0,len(weights)):
                if W == 0:
                        return V
                else:
                        density = list(map(truediv, values, weights))
                        i = density.index(max(density))
                        a = min(weights[i],W)
                        V = V + a*values[i]/weights[i]
                        weights[i] = weights[i] - a
                        W = W-a	
                        if weights[i] <= 0:
                        	values.remove(values[i])
                        	weights.remove(weights[i])
        return V

#Test Case
# capacity = 10
# weights = [30, 1, 2]
# values = [50000000,10, 30]
# print(get_optimal_value(capacity, weights, values))

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
