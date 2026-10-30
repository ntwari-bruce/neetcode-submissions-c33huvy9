from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            # here because sorted by itself returns fragmented thing.
            sortedWord = "".join(sorted(word))
            anagrams[sortedWord].append(word)
        
        return list(anagrams.values())
           
   

        