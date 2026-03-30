from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # aiming for O(n+m) time complexity and O(1) space complexity
        # start with a brute force solution
        #sorted_s = "".join(sorted(s))
        #sorted_t = "".join(sorted(t))
        #return sorted_s == sorted_t

        # using to hashtables
        count_s = defaultdict(int)
        count_t = defaultdict(int)

        for char in s:
            count_s[char] += 1
        
        for char in t:
            count_t[char] += 1
        
        return count_s == count_t
    



        