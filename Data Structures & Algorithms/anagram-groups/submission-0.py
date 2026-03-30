from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # the ideo is that after sorting this certain word,
        # does it look like this other word
        # {"cat": [act]}
        anagrams = defaultdict(list)
        # iterate through the string
        for s in strs:
            sorted_word = "".join(sorted(s))
            anagrams[sorted_word].append(s)
        
        return list(anagrams.values())


        