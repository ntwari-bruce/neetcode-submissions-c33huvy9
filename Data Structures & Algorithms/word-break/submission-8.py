class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # define the dfs function
        cache = {}

        def dfs(i):
            if i in cache:
                return cache[i]
            # if we have reached the end of the input word
            if i == len(s):
                return True
            
            # we iterate through each word in the dictionary
            # or if the words are matching
            # if the condition is true, we're going to retursively check other words in the input string
            for word in wordDict:
                if i + len(word) <= len(s) and s[i : i + len(word)] == word:
                    if dfs(i + len(word)):
                        cache[i] = True
                        return True
            
            # if for some reason we hit all the words without the pointer i being equal to the lenght of the words
            cache[i] = False
            return False
        
        return dfs(0)


