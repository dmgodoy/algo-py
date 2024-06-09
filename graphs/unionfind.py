# For disjoint set of nodes, we build trees that are not necessarily accurate with
# the graph, we try to keep them balanced instead to make the find operation efficient
# Uses:
# Find if a graph has a cycle
# Find number of connected components

class UnionFind():
    def __init__(self, n: int):
        self.par = {}
        self.rank = {}
        for i in range(n):
            self.par[i] = i
            self.rank[i] = 1
    def union(self, n1: int, n2: int) -> bool:
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2: return False
        if self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        elif self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        else:
            self.par[p1] = p2
            self.rank[p2] += 1 # this is the only case where we need to adjust rank
        return True
    
    def find(self, n: int) -> int:
        curr = n
        while self.par[curr] != curr:
            self.par[curr] = self.par[self.par[curr]] # path compression 
            curr = self.par[curr]    
        return curr         

uf1 = UnionFind(3)
for e1,e2 in [[0,1],[1,2],[0,2]]: # edges, has cycle
    if not uf1.union(e1, e2):
        print(f'cycle detected with edge: {e1} -> {e2}') # cycle detected with edge: 0 -> 2

print(f'{len(set(uf1.par.values()))} disjoint sets') # 1 disjoint sets

uf2 = UnionFind(3)
for e1,e2 in [[0,1]]: # only one edge
    if not uf2.union(e1, e2):
        print(f'cycle detected with edge: {e1} -> {e2}')
print(f'{len(set(uf2.par.values()))} disjoint sets') # 2 disjoint sets

