# min spanning tree cost 
# prims
import heapq

# min heap will contain a max of E total num of edges
# time complexity E*log(E)
# E = V^2 => log(E) = log(V^2) = 2*log(V)
# time complexity:  O(E*log(V))
# space complexity: O(E)

def min_spanning_tree_cost(edges: list[int], n: int) -> int:
    adj = {i: [] for i in range(1, n + 1)}
    for u,v,w in edges:
        adj[u].append([w,v])
    minheap = [[0, 1]]
    visited = set()
    res = 0


    while minheap:
        w,u = heapq.heappop(minheap)
        if u in visited:
            continue
        visited.add(u)
        res += w
        for wei, nei in adj[u]:
            if not nei in visited:
                heapq.heappush(minheap, [wei, nei])
    return res
edges = [[1,2,3],[1,3,5],[1,4,6],[2,3,1],[3,2,2],[3,4,1]]
n = 4
print(min_spanning_tree_cost(edges, n)) # 5