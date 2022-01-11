class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        char_map = {}
        res = -1
        for i, c in enumerate(s):
            if c not in char_map:
                char_map[c] = i
            else:
                res = max(res, i - char_map[c] - 1)
        
        return res