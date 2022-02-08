class TreeAncestor:

    def __init__(self, n: int, p: List[int]):
        self.logn = math.ceil(math.log2(n)) + 1
        self.n = n
        
        ancestor = [[-1 for i in range(self.n)] for j in range(self.logn)]
        
        for i in range(n):
            ancestor[0][i] = p[i]
        
        for i in range(1, self.logn):
            for j in range(n):
                if ancestor[i-1][j] != -1:
                    ancestor[i][j] = ancestor[i-1][ancestor[i-1][j]]
        
        
        self.ancestor = ancestor
        

    def getKthAncestor(self, node: int, k: int) -> int:
        
        for i in range(self.logn):
            mask = 1 << i
            
            if node == -1:
                break
            
            if k & mask: 
                node = self.ancestor[i][node]
        
        return node
        


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)