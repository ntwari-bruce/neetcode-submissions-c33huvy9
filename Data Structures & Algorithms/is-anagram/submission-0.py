class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # aiming for O(n+m) time complexity and O(1) space complexity
        # start with a brute force solution
        sorted_s = "".join(sorted(s))
        sorted_t = "".join(sorted(t))
        return sorted_s == sorted_t
        