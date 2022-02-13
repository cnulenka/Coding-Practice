class BrowserHistory:

    def __init__(self, homepage: str):
        self.back_stack = [homepage]
        self.forward_stack = []

    def visit(self, url: str) -> None:
        self.back_stack.append(url)
        self.forward_stack.clear() 

    def back(self, steps: int) -> str:
        top = None
        for i in range(steps):
            if len(self.back_stack) > 1:
                top = self.back_stack.pop()
                self.forward_stack.append(top)
        
        return self.back_stack[-1]

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if self.forward_stack:
                top = self.forward_stack.pop()
                self.back_stack.append(top)

        return self.back_stack[-1]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)