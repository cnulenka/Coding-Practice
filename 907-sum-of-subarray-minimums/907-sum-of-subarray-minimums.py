class Solution:
    def sumSubarrayMins(self, A):
        res = 0
        stack = []  #  non-decreasing # tricky, # mutilple qs based on this
        A = [float('-inf')] + A + [float('-inf')]
        for i,n in enumerate(A):
            # push to stack when stack top is smaller than curr num
            while stack and n < A[stack[-1]]:
                curr = stack.pop()
                res += A[curr] * (i-curr) * (curr - stack[-1])
            stack.append(i)
        # print(res)
        return res % (10**9 + 7)