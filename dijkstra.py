import sys
from math import inf
from heapq import heappop, heappush
from collections import defaultdict

def dijkstra(G, s):
    # initialize:
    # set shortest[source] = 0, shortest[other nodes] = infinity
    shortest = {}
    for k, v in G.items():
        shortest[k] = inf
        for kk in v.keys():
            shortest[kk] = inf
    # initially, queue contains source node
    q = [(0, s)]
    while q:
        # while queue is not empty, extract the node with shortest path from queue
        p, v = heappop(q)
        # if v is unvisited, record the shortest path to v into shortest{}
        if shortest[v] == inf:
            shortest[v] = p
            if v in G:
                for w, vw in G[v].items():
                    # for each node w adjacent to v, if unvisited, push to queue
                    if shortest[w] == inf:
                        heappush(q, (shortest[v] + vw, w))
        pass
    return shortest
    pass

def main():
    G = {
        'b': {'e': 0}, 
        'c': {'h': 15, 'f': 8, 'g': 9}, 
        'f': {'d': 0}, 
        'a': {'b': 1, 'f': 10, 'c': 2, 'g': 11}, 
        'g': {'c': 0}, 
        'd': {'h': 14, 'f': 6, 'g': 7}, 
        'e': {'h': 9, 'f': 1, 'g': 3}
    }
    shortest = dijkstra(G, 'a')
    print(shortest)
    pass

if __name__ == "__main__":
    sys.exit(main())