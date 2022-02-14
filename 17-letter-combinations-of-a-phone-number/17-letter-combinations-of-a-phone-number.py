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
        
        def computeCombinations(new_str, id):
            nonlocal digits, res
            #print(new_str, id)
            
            if id == len(digits):
                res.append(new_str)
                return
            
            chars = self.getDigitToCharsMap(digits[id])
            
            for i in range(len(chars)):
                computeCombinations(new_str+chars[i], id+1)
        
        computeCombinations("", 0)
        
        return res