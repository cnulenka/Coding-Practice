# public class Solution {
#     public List<Integer> lexicalOrder(int n) {
#         List<Integer> res = new ArrayList<>();
#         for(int i=1;i<10;++i){
#           dfs(i, n, res); 
#         }
#         return res;
#     }
    
#     public void dfs(int cur, int n, List<Integer> res){
#         if(cur>n)
#             return;
#         else{
#             res.add(cur);
#             for(int i=0;i<10;++i){
#                 if(10*cur+i>n)
#                     return;
#                 dfs(10*cur+i, n, res);
#             }
#         }
#     }
# }

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        
        def dfs(curr, n):
            nonlocal res
            if curr > n:
                return
            else:
                res.append(curr)
                for i in range(10):
                    temp = 10*curr+i
                    if temp > n:
                        return
                    dfs(temp, n)
        
        res = []
        for i in range(1,10):
            dfs(i,n)
        
        return res