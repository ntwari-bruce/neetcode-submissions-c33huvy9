class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # we're populating the max-sub sequence at each index
        # at each index we're taking the max of it (1) and
        # the max of it(1) added with the next max
        LIS = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            # here we're iterating to find the longest increasing
            # EX: [1,2,3,4]
            # Start at 4, put 1, start at 3, iterate finding max
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        

        return max(LIS)

        # TIME COMPLEXITY O(n^2)
        # SPACE COMPLEXITY O(N)
            
        