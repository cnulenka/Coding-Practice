class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList or not beginWord or not endWord or not wordList:
            return 0
        
        all_word_dict = defaultdict(list)
        
        for word in wordList: # N
            for i in range(len(word)): # M
                new_word = word[:i] + "*" + word[i+1:] # M -> N*M^2
                all_word_dict[new_word].append(word)
        
        queue = collections.deque([(beginWord, 1)])
        visited = {beginWord: True}
        
        while queue:
            curr_word, length = queue.popleft()
            if curr_word == endWord:
                return length
            
            for i in range(len(curr_word)): # M
                new_word = curr_word[:i] + "*" + curr_word[i+1:] # M -> M^2
                for word in all_word_dict[new_word]: # loop through neighbors
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, length+1))
                
                # make it empty as this word has been visited
                all_word_dict[new_word] = []
        
        return 0