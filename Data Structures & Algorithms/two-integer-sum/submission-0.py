class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # have indecies of the numbers
        indicies = {}
        for i, n in enumerate(nums):
            indicies[n] = i
        
        for i, num in enumerate(nums):
            diff = target - num
            if diff in indicies and indicies[diff] != i:
                return [i, indicies[diff]]
        



        