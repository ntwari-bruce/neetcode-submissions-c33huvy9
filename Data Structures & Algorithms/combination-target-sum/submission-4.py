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

        # for these type of questions, we're making two decisions at
        # every stage, so the tree growns by the height of the tree
        # 2 ^ target/minimum, the same for the space because the space
    # space goes with the height of the tree.