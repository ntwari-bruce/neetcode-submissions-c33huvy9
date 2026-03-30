class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # My second solution
        res = []
        nums.sort()
        def backtrack(i, subset):
            # the basecase
            if i == len(nums):
                res.append(subset.copy())
                return
            
            # all subsets that include nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)

            # all subsets that don't include the nums[i]
            subset.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, subset)
        
        backtrack(0, [])
        return res
