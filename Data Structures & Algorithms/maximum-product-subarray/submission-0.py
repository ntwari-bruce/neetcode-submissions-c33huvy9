class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # the brute force solution
        
        # we initialize the res as the first element
        # because we might have an array with just one element
        res = nums[0]

        for i in range(len(nums)):
            curr = nums[i]
            res = max(res, curr)
            for j in range(i + 1, len(nums)):
                curr *= nums[j]
                res = max(res, curr)
        
        return res

        