#User function Template for python3

class Solution:
    def removeConsecutiveCharacter(self, S):
        
        s = [S[0]]
        
        for i in range(1, len(S)):
            
            if s and s[-1] == S[i]:
                continue
            else:
                s.append(S[i])
                
        
        return "".join(s)
                
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        s = input()
        ob = Solution()
        print(ob.removeConsecutiveCharacter(s))

# } Driver Code Ends