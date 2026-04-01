class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        # the one edge case, assuming we have reached the eend of s
        dp[len(s)] = True
        for i in range(len(s)-1, -1, -1):
            for word in wordDict:
                if i + len(word) <= len(s) and s[i: i+len(word)] == word:
                    dp[i] = dp[i + len(word)]
                
                if dp[i]:
                    break
        

        # after reaching the end on the s, we check the boolean
        return dp[0]
