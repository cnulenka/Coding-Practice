class MinStack:
    
    # check leetcode solution
    # push (val, min) to stack
    # maintain curr_min with every element
    
    # or trick
    # val < min
    # val + val < min + val
    # 2val < min + val
    # 2val - min < val # convert it into a number so that it becomes
    # even less than value
    

    def __init__(self):
        self.stack = []
        self.min = -1

    def push(self, val: int) -> None:
        #print(self.min)
        if not self.stack:
            self.min = val
            self.stack.append(val)
        else:
            if val > self.min:
                self.stack.append(val)
            else:
                self.stack.append(2*val - self.min)
                self.min = val
        #print(self.stack)

    def pop(self) -> None:
        #print("pop", self.min)
        top = self.stack[-1]
        self.stack.pop()
        if self.min > top:
            self.min = 2*self.min - top
        #print("pop", self.min)
        
    def top(self) -> int:
        top = self.stack[-1]
        if top < self.min:
            return self.min
        return top

    def getMin(self) -> int:
        return self.min