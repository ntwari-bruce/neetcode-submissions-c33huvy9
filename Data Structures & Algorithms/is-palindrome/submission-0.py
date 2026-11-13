class Solution:
    def isPalindrome(self, s: str) -> bool:
        # first filter the string to remain with only alphanumerical
        # abc
        # "abdc"
        new_s = ""
        for char in s:
            if char.isalnum():
                new_s = new_s + char.lower()
        
        n = len(new_s)
        i = 0
        j = n - 1
        while i < j:
            if new_s[i] != new_s[j]:
                return False
            i += 1
            j -= 1
        
        return True
                
