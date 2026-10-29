class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # start with brute force solution
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i < j and nums[i] + nums[j] == target:
                    return [i, j]



        