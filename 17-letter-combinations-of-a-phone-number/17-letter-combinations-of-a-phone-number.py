class Solution:
    def getDigitToCharsMap(self, key):
        char_map = {
            '0': ' ',
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }
        return char_map[key]

    def letterCombinations(self, digits: str) -> List[str]:

        res = []
        
        if not digits:
            return res
        
        def combinations(curr_str, ind):
            
            if ind == len(digits):
                res.append(str(curr_str))
                return
            
            chars = self.getDigitToCharsMap(digits[ind])
            
            for char in chars:
                combinations(curr_str+char, ind+1)
        
        
        combinations("", 0)
        return res