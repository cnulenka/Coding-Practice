#User function Template for python3

'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def findDist(self,root,a,b):
    
        def findLca(root, a, b):
            
            if root == None or root.data == a or root.data == b:
                return root
            
            
            left = findLca(root.left, a, b)
            right = findLca(root.right, a, b)
            
            #print(left)
            #print(right)
            
            if not left:
                return right
            elif not right:
                return left
            else:
                return root
        
        def distanceFromRoot(root, data):
            
            if not root:
                return 0
                
            #print(root.data)
            if root.data == data:
                #print(data)
                return 1
            
            
            left = distanceFromRoot(root.left, data)
            right = distanceFromRoot(root.right, data)
            
            #print(left, right)
            
            if not left and not right:
                return 0
            
            if left:
                return left + 1
            
            if right:
                return right + 1
        
        
        lca = findLca(root, a, b)
        #print(lca.data)
        dis1 = distanceFromRoot(lca, a) - 1
        dis2 = distanceFromRoot(lca, b) - 1
        
        #print(dis1,dis2)
        
        return  dis1 + dis2
        
        
        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(50000)
from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root


if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        a, b=map(int, input().split())
        ob = Solution()
        print(ob.findDist(root, a, b))

# } Driver Code Ends