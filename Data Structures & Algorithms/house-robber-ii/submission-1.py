class Solution:
    def rob(self, nums: List[int]) -> int:
        # reuse the house robber I on this
        # take the maximum when we ignore the first and last
        # return max
        # [rob1, rob2, n, n + 1, ....]
        if len(nums) == 1: # the edge case when we only have just element
            return nums[0]

        n = len(nums)
        return max(self.robber(nums[1:]), self.robber(nums[: n - 1]) )

    def robber(self, nums):
        rob1, rob2 = 0, 0
        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp # in otherwords rob2 will be temp i.e the max we can rob up to that point

        return rob2