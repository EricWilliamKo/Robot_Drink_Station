
from collections import defaultdict
from heapq import *
import csv

def dijkstra(pathdic, f, t):
    pathBuf = list()
    q, seen = [(0,f,pathBuf)], set()
    while q:
        (cost,v1,path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path.append(v1)
            if v1 == t: return (cost, path)

            for c, v2 in pathdic.get(v1, ()):
                if v2 not in seen:
                    dicpath = path[0:]
                    heappush(q, (cost+c, v2, dicpath))
                    dicpath = []

    return float("inf")

def tupleToDic(tu):
    result = []
    result.insert(0,tu[0])
    while tu[1] is not ():
        tu = tu[1]
        result.insert(0,tu[0])
    return result



if __name__ == "__main__":
    pathfile = open('path.csv','rb')
    pathdic = defaultdict(list)
    reader = csv.reader(pathfile,dialect = 'excel')
    for l,r,c in reader:
        pathdic[l].append((int(c),r))
    

    print dijkstra(pathdic, 'L1', 'S1')
    
