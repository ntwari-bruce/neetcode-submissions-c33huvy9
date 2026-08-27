class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combinations = []

        def dfs(i, sub_comb, target):
            # if we found it
            if sum(sub_comb) == target:
                combinations.append(sub_comb.copy())
                return
            # base cases
            if sum(sub_comb) > target or i >= len(nums):
                return
            
            sub_comb.append(nums[i])
            dfs(i, sub_comb, target)

            # if we return
            sub_comb.pop()
            # then we move on to the next 
            dfs(i + 1,sub_comb, target)
        dfs(0, [], target)
        return combinations