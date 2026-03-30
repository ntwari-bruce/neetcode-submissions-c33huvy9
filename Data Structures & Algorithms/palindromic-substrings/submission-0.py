class Solution:
    def countSubstrings(self, s: str) -> int:
        numSub = 0

        for i in range(len(s)):
            for j in range(i, len(s)):
                l, r = i, j
                while l < r and s[l] == s[r]:
                    l += 1
                    r -= 1
                
                if l >= r:
                    numSub += 1
        # return the num of substring
        return numSub

        