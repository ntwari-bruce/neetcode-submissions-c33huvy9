class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # we're returning the number of ways we can reach the target while adding and subtracting
        def backtrack(i, curr_sum):
            if i == len(nums):
                if curr_sum == target:
                    return 1
                else:
                    return 0
            
            left = backtrack(i + 1, curr_sum + nums[i])
            right = backtrack(i + 1, curr_sum - nums[i])

            return left + right
        
        return backtrack(0,0)
        



        