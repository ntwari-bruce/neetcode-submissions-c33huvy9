class Solution:
    def climbStairs(self, n: int) -> int:
        # say this is the array 
        # [1,2,3,4,5]
        # one point 4
        # two point at 5
        # after initializing two values one, and two, 
        # we're computing up to n-1,

        one, two = 1, 1
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        
        return one
        # time complexity is O(n)
        # space complexity  is O(1)

        