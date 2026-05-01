class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # prefix captures product of subarray from 0 to right
        # suffix captures products of subarray from last index back to zero
        res = nums[0]
        n = len(nums)
        prefix = suffix = 0
        # (prefix or 1) it helps to reset prefex to 1 when the product is 0


        for i in range(n):
            prefix = nums[i] * (prefix or 1)
            suffix = nums[n - i - 1] * (suffix or 1)
            res = max(res, max(prefix, suffix))
        
        return res
        