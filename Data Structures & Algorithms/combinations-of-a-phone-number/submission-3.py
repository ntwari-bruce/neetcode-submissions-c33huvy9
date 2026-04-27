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

        def dfs(i, curr):
            # base case
            if len(digits) == len(curr):
                res.append(curr)
                return
            
            for c in digitToChar[digits[i]]:
                dfs(i + 1, curr + c)
        if digits:
            dfs(0, "")
        
        return res

        # time complexity
        # at each digit, we branch into 4 letter( worst case )
        # for n digits, we have 4^n leaf nodes
        # for res.append(curr) it take O(n) to copy the string
        # overall time complexity O(n * 4^n)


        # space complexity
        # the recursion stack goes down n levels O(n)
        # curr is at most O(n)
        # we have 4^n combinations total in the output string with each combination n
        # O(4^n * n)
        
