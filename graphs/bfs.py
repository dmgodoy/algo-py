from collections import deque


edges = [[1,2],[1,3],[1,4],[4,1],[2,5],[3,5],[3,7]]
n = 7
adj = {}
for i in range(1, n + 1):
    adj[i] = []
for u,v in edges:
    adj[u].append(v)
print(adj)

q = deque([1])
visited = set([1])
res = []
while q:
    size = len(q)
    for _ in range(size):
        u = q.popleft()
        res.append(str(u))
        for nei in adj[u]:
            if nei not in visited:
                q.append(nei)
                visited.add(nei)
print(" -> ".join(res))


