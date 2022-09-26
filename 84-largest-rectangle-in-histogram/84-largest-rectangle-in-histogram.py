class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        if not len(heights):
            return 0
        
        stack = [-1]
        max_area = 0
        i = 0
        
        while i<n:
            #print(i, stack)
            # increasing stack
            # pop if u get someone smaller
            # thats the end of rectangle with stack[-1] height
            # so u get left end and right end
            # get the width and calculate the area
            while stack[-1] !=-1 and heights[stack[-1]] >= heights[i]:
                #print(stack)
                curr_height = heights[stack.pop()]
                curr_width = i - 1 - stack[-1]
                area =  curr_height * curr_width
                #print(area)
                max_area = max(area, max_area)
            stack.append(i)
            i += 1
        
        #print('########')
        while stack[-1] !=-1:
            #print(stack)
            curr_height = heights[stack.pop()]
            # here N - 1 not i - 1
            curr_width = n - 1 - stack[-1]
            area =  curr_height * curr_width
            #print(area)
            max_area = max(area, max_area)
        
        
        return max_area