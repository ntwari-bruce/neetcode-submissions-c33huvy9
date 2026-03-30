class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
       
       
       
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i, curr):
            # the base case 
            if len(digits) == len(curr):
                res.append(curr)
                return
            
            # for the character of the first index(in 23 it is 2)
            # for each character add characters of others, and move on to the next character. 
            for c in digitToChar[digits[i]]: 
                backtrack(i + 1, curr + c) # after we backtrack we come here and have what we had earlier.
        
        if digits:
            backtrack(0, "")
        
        return res

        # time complexity: say we have worst input 9999 and 9 maps to "wxyz", for each we have 4 combinations
        # The length of each output string will be equal to n giving O(n * 4^n)
        # the same for extra space.  
        


        