class Solution:
    def longestPalindrome(self, s: str) -> str:
        # when checking palindrom
        # start in the middle and expand outwardly 
        # checking characters to the left, and to the right
        # it is difference for even and odd
        res = ""
        resLength = 0

        for i in range(len(s)):
            # for odd palindromes
            l, r = i, i
            # meaning if it is a palindrome
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLength:
                    resLength = r - l + 1
                    res = s[l: r + 1]
                # update the pointers
                l -= 1
                r += 1
            
            # for even lengths
            l, r = i, i + 1
            # meaning if it is a palindrome
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLength:
                    resLength = r - l + 1
                    res = s[l: r + 1]
                # update the pointers
                l -= 1
                r += 1
        
        return res

        # The brute for has time complexity of O(n^3)
        # This has a time complexity of O(n^2)
                