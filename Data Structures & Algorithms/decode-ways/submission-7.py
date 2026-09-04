class Solution:
    def numDecodings(self, s: str) -> int:
        # solve the question using dfs

        cache = {}

        def dfs(i):
            # two base bases
            # if we reach the end, or dead end, return 1 to that
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0

            if i in cache:
                return cache[i]
            # take one digit
            cache[i] = dfs(i + 1)

            # after we return from the single digit, try to take two digits
            # we check if we're within the bounds
            if i < len(s) - 1:
                # here we're checking if this two digit is valid
                if s[i] == "1" or (s[i] == "2" and s[i + 1] < "7"):
                    cache[i] += dfs(i + 2)
            
            return cache[i]
        
        return dfs(0)


        # this is a tree to better understand what is happening
        '''                          "226"
                        /       \
                  bite "2"      bite "22"
                    /               \
                 "26"               "6"
               /      \              |
         bite "2"    bite "26"    bite "6"
            /            \           |
          "6"            ""          ""
           |             ✓           ✓
        bite "6"
           |
           ""
           ✓.      '''



       