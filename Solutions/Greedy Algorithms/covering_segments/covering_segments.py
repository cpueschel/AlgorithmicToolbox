# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def update(lists, to_drop):
    new_list = []
    for i in range(len(lists)):
        if i not in to_drop:
            new_list.append(lists[i])
    return new_list
     
def optimal_points( startpoints,endpoints):
    points = []
    # startpoints = list(map(lambda x: x[0], segments))
    # endpoints = list(map(lambda x: x[1], segments))
    for i in range(len(startpoints)):
        if startpoints == []:
            return points
        ii = endpoints.index(min(endpoints))
        points.append(endpoints[ii])    
        to_drop = []
        for iii in range(len(startpoints)):            
            if startpoints[iii] <= endpoints[ii] <= endpoints[iii]:
                to_drop.append(iii)
        if to_drop:
            startpoints = update(startpoints, to_drop)
            endpoints = update(endpoints, to_drop)
    return points

#Test Case
# startpoints=[1,2,3]
# endpoints=[3,5,6]
# print(optimal_points(startpoints,endpoints))

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    startpoints = data[::2]
    endpoints = data[1::2]
    points = optimal_points(startpoints,endpoints)
    print(len(points))
    for p in points:
        print(p, end=' ')
