class Node:
    
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.right = self.left = None
    
    def insert(self, node):
        if node.start >= self.end:
            if not self.right:
                self.right = node
                return True
            return self.right.insert(node)
        elif node.end <= self.start:
            if not self.left:
                self.left = node
                return True
            return self.left.insert(node)
        else:
            return False

class MyCalendar:

    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        node = Node(start, end)
        if not self.root:
            self.root = node
            return True
        return self.root.insert(node)


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)