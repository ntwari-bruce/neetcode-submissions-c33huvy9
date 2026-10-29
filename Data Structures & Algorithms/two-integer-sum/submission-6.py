class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # solution using two hash maps
        indices = {} # val -> indeces
        for i, n in enumerate(nums):
            indices[n] = i
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]
        return []