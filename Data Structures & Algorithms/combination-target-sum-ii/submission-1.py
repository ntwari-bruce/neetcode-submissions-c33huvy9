class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, curr, total):
            # first base case
            # if total is equal to the target
            if total == target:
                res.append(curr.copy())
                return
            
            # base case #2, if we run out of candidates, or go over total
            if total > target or i == len(candidates):
                return

            
            curr.append(candidates[i])
            dfs(i + 1, curr, total + candidates[i])

            # on other side of tree
            curr.pop()

            # skip the identical elements, cz we have duplicates
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            
            dfs(i + 1, curr, total)
        dfs(0, [], 0)
        return res

        # Time complexity
    #------------------------
    # we have two choices per element making a total of 2^n combinations
    # for the copy() the worst case O(n)
    # total time complexity O(n * 2^n)
    # the reason we don't use O(2^n) in combination sum one is because we are reusing an element 
    # we're not using an element one, in worst case the input can be [1,1,1,1,1] and we'd have
    # to keep reusing it as we move forward
         

