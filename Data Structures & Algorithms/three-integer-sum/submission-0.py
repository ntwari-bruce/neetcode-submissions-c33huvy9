class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # we have to sort the numbers first
        nums.sort()
        res = []
        for i, a in enumerate(nums):
            # if a is positive means the rest are positive
            if a > 0:
                break
            # here we're skipping duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                threeSome = a + nums[l] + nums[r]
                if threeSome > 0:
                    r -= 1
                elif threeSome < 0:
                    l += 1
                # this is where it is 0
                else:
                    temp = [a, nums[l], nums[r]]
                    res.append(temp)
                    l += 1
                    r -= 1
                    # check for l duplicate or r
                    # skipping either l or r will give 
                    # Different results for a hence avoiding duplicated
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        
        return res






        