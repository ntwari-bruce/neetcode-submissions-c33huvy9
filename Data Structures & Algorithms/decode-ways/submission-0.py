class Solution:
    def numDecodings(self, s: str) -> int:
        # dp = {len(s): 1} because we are taking dp[i] = dp[i+1]
        # Meaning let's say 12, when we reach 2, there is one way to decode it
        # NOt that an empty string have some meaning

        # start at the end and ask, how many ways can we
        # decode starting at index 

        dp = {len(s): 1}
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]
            
            # if we reach double digits
            if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"):
                dp[i] += dp[i + 2]
        
        return dp[0]


        
        