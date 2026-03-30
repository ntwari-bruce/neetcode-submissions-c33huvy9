class Solution:
    def rob(self, nums: List[int]) -> int:
        # say we have an array [1, 2, 3, 1]
        # cutting at 1( index 0 ), [1| we can just rob it
        # cutting at 2( index 1 ), [1,2| we can either rob 2, or rob 1, so that max is 2, we choose it
        # cutting at 3( index 2 ), [1,2,3| we can either rob 3 + 1, or 2(in otherwords, 3 + 1 vs max from the previous others not including 3(adjacent))
        # cutting at 1( index 3 ), [1,2,3,1| we can rob 1 + 2, vs the max we can get from others but not including 1 because it is adjacent

        rob1, rob2 = 0, 0

        # [rob1, rob2, n, n n+1, ...]
        for n in nums:
            curr_max = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = curr_max # this is where we can skip the next value and choose this max
        
        return rob2

