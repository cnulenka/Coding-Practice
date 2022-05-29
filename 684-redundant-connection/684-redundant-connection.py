class DSU:
    def __init__(self):
        self.parent = list(range(1001))
        self.rank = [0] * 1001
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        xp, yp = self.find(x), self.find(y)
        if xp == yp:
            return False
        if self.rank[xp] > self.rank[yp]:
            self.parent[yp] = xp
        elif self.rank[xp] < self.rank[yp]:
            self.parent[xp] = yp
        else:
            self.parent[xp] = yp
            self.rank[yp] += 1
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU()
        for edge in edges:
            if not dsu.union(*edge):
                return edge
                