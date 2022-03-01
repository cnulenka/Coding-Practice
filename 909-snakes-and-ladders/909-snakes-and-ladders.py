class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        def num_to_loc(label):
            r, c = divmod(label-1, n)
            if r % 2 == 0:
                return n-1-r, c
            else:
                return n-1-r, n-1-c
        
#         def num_to_loc(num):
#             loc_dic = {
#                 1 : (5,0), 2 : (5,1), 3 : (5,2), 4 : (5,3), 5 : (5,4), 6 : (5,5),
#                 12 : (4,0), 11 : (4,1), 10 : (4,2), 9 : (4,3), 8 : (4,4), 7 : (4,5),
#                 13 : (3,0), 14 : (3,1), 15 : (3,2), 16 : (3,3), 17 : (3,4), 18 : (3,5),
#                 24 : (2,0), 23 : (2,1), 22 : (2,2), 21: (2,3), 20 : (2,4), 19 : (2,5),
#                 25 : (1,0), 26 : (1,1), 27 : (1,2), 28 : (1,3), 29 : (1,4), 30 : (1,5),
#                 36 : (0,0), 35 : (0,1), 34 : (0,2), 33 : (0,3), 32 : (0,4), 31 : (0,5),
#             }
            
#             #print(num)
#             return loc_dic[num]
    
        q = collections.deque()
        q.append((1, 0))
        visited = set()
        moves = 0
        while q:
            #print(q)
            for i in range(len(q)):              
                pos, m = q.popleft()
                
                x, y = num_to_loc(pos)
                
                if board[x][y] != -1:
                    pos = board[x][y]
                
                if pos == n*n:
                    return moves
                
                
                for j in range(1,7):
                    next_pos = pos + j
                    if next_pos <= n*n and next_pos not in visited:
                        visited.add(next_pos)
                        q.append((next_pos, m+1))
            moves += 1
        return -1
            
        