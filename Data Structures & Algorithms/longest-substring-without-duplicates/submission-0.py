class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        found_letter = set()
        l, r = 0, 0
        max_length = 0

        while r < len(s):
            if s[r] not in found_letter:
                found_letter.add(s[r])
                max_length = max(max_length, r - l + 1)
                r += 1
            else:
                while s[r] in found_letter:
                    found_letter.remove(s[l])
                    l += 1
        
        return max_length

        