class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # if the total sum is odd, impossible to split with integers
        # the idea is that i dp we'll fill in take it or leave it
        # in dp, we are adding all the subsets sum reachable up to that number
        # say we're {0, 5}
        if sum(nums) % 2:
            return False
        
        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums) - 1, -1, -1):
            nextDp = set()
            for t in dp:
                nextDp.add(t + nums[i])
                nextDp.add(t)
            
            dp = nextDp
        
        return True if target in dp else False

        