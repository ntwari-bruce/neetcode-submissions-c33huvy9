class Solution:

    def encode(self, strs: List[str]) -> str:

       # "3#neet3#coo"
       # we'll have length, #, and that string
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            # when we reach #, we stop there
            while s[j] != "#":
                j += 1
            
            # we have reached j
            length = int(s[i:j])
            # "3#neet3#coo"
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res

        
                



