# find shortest path
import heapq
def dijkstra(n: int, edges: list[list[int]], start: int) -> dict: 
    #build adj list
    adj = {}
    for v in range(0, n):
        adj[v] = []
    for src, dst, weight in edges:
        adj[src].append([dst, weight])
    
    shortest = {}
    minheap = [[0, start]]
    while minheap:
        w1, n1 = heapq.heappop(minheap)
        if n1 in shortest: continue
        shortest[n1] = w1
        for n2, w2 in adj[n1]:
            if n2 not in shortest:
                heapq.heappush(minheap, [w1 + w2, n2])
    for i in range(0, n):
        if not i in shortest:
            shortest[i] = -1

    return shortest
# node 0 -> 1 d = 3
# node 0 -> 2 d = 1
# node 2 -> 1 d = 1
print(dijkstra(3, [[0,1,3],[0,2,1],[2,1,1]], 0))



