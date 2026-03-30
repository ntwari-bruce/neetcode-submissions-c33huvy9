class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        # taking the starting index
        def dfs(i):
            # base case
            if i >= len(s):
                res.append(part.copy())
            
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    part.append(s[i: j + 1])
                    dfs(j + 1) # we move the starting point.
                    # clean the partition array
                    part.pop()
        dfs(0)
        return res
        
    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        
        return True
    

        # say we have "aab", we process a, a, b, ab, aa, aab, b, 
        # here we are going to have a, a, b, ab, b as the results
        # we're poping part to remove what we have just added on the 
        # top

        # we have possible 2^n partitions from each position
        # we O(n) for palindrome checking
        # this give O(n * 2^n) overall complexity

        # we have O(n) for recursion stack
        # we have 2^n for the output 
        # resulting in O(n * 2^n) for the space complexity
        



        