class TrieNode:
    
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            # create the entry if doesn't exist else return entry
            current = current.children[char]
        current.is_end = True
    
    def search(self, word: str) -> bool:
        node = self.startsWith(word)
        return node and node.is_end

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for char in prefix:
            current = current.children.get(char)
            if not current:
                return None
        return current


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)