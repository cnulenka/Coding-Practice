class DLL:
    
    def __init__(self):
        self.key = 0
        self.val = 0
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head = DLL()
        self.tail = DLL()
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def insert_at_head(self, node):
        temp = self.head.next
        temp.prev = node
        node.next = temp
        self.head.next = node
        node.prev = self.head
    
    def delete_from_tail(self):
        del_node = self.tail.prev
        self.delete_node(del_node)
        self.cache.pop(del_node.key)
        del del_node
        
    def move_to_head(self, node):
        self.delete_node(node)
        self.insert_at_head(node)
        

    def get(self, key: int) -> int:
        #print(self.cache)
        if key in self.cache:
            node = self.cache[key]
            self.move_to_head(node)
            return node.val
        
        return -1
    
    def delete_node(self, node):
        prev = node.prev
        nextt = node.next
        
        prev.next = nextt
        nextt.prev = prev
    
    def add_node(self, key, value):
        node = DLL()
        node.val = value
        node.key = key
        
        self.cache[key] = node
        self.insert_at_head(node)

    def put(self, key: int, value: int) -> None:
        #print(self.cache)
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.move_to_head(node)
        else:
            if self.size + 1 > self.capacity:
                self.delete_from_tail()
            else:
                self.size += 1
            
            self.add_node(key, value)
            

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)