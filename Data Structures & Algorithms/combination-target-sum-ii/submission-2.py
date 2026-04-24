class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # sort the input
        combinations = []
        candidates.sort()

        def dfs(i, curr, total):
            # base case 2
            if total == target:
                combinations.append(curr.copy())
                return
            # base case 1:
            if i == len(candidates) or total > target:
                return
            
            curr.append(candidates[i])
            dfs(i + 1, curr, total + candidates[i])

            # when we backtrack
            curr.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            
            dfs(i + 1, curr, total)
        
        dfs(0,[],0)
        return combinations
        
        # time complexity O(n * 2^n)
        # space complexity O(n) for the recursion depth in worst case