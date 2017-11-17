
from collections import defaultdict
from heapq import *

def dijkstra(edges, f, t):
    g = defaultdict(list)
    for l,r,c in edges:
        g[l].append((c,r))
    pathBuf = list()
    q, seen = [(0,f,pathBuf)], set()
    # q, seen = [(0,f,())], set()
    while q:
        # path = []
        (cost,v1,path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path.append(v1)
            # path = (v1,path)
            if v1 == t: return (cost, path)

            for c, v2 in g.get(v1, ()):
                if v2 not in seen:
                    path2 = path[0:]
                    heappush(q, (cost+c, v2, path2))
                    path2 = []

    return float("inf")

def tupleToDic(tu):
    result = []
    result.insert(0,tu[0])
    while tu[1] is not ():
        tu = tu[1]
        result.insert(0,tu[0])
    return result



if __name__ == "__main__":
    edges = [
        ('S1','P1',1),('S2','P2',1),('S3','P3',1),('S4','P4',1),('S5','P5',1),('S5I','P5I',1),
        ('L1','P6',1),('L2','P7',1),('L3','P8',1),
        ('P1','P2',1),('P1','P2',1),('P2','P3',1),('P3','P4',1),('P4','P5',1),
        ('P6','P7',1),('P7','P8',1),
        ('P0','P1',3),('P0','P2',3),('P0','P3',3),('P0','P4',3),('P0','P5',3),('P0','P5I',3),
        ('P0','P6',3),('P0','P7',3),('P0','P8',3),
        ('P1', 'S1', 1), ('P2', 'S2', 1), ('P3', 'S3', 1), ('P4', 'S4', 1), ('P5', 'S5', 1), ('P5I', 'S5I', 1), ('P6', 'L1', 1), ('P7', 'L2', 1), ('P8', 'L3', 1), ('P2', 'P1', 1), ('P2', 'P1', 1), ('P3', 'P2', 1), ('P4', 'P3', 1), ('P5', 'P4', 1), ('P7', 'P6', 1), ('P8', 'P7', 1), ('P1', 'P0', 3), ('P2', 'P0', 3), ('P3', 'P0', 3), ('P4','P0', 3), ('P5', 'P0', 3), ('P5I', 'P0', 3), ('P6', 'P0', 3), ('P7', 'P0', 3), ('P8', 'P0', 3)
    ]

    edges2 = []
    for edge in edges:
        edges2.append((edge[1],edge[0],edge[2]))
    # print edges2

    print "=== Dijkstra ==="
    (cost, path) = dijkstra(edges, 'S5', 'S5I')
    print dijkstra(edges, 'S5', 'S5I')
    # dicpath = tupleToDic(path)
    # print dicpath
