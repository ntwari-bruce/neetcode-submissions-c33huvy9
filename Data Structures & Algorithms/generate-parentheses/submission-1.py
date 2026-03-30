class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # we have 3 conditions
        # only add open paranthesis if open < n
        # only add close paranthesis is close < open
        # valid if open = close = n
        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()

            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0,0)
        return res

        # time complexity
        # O(4^n / root(n))

        # Space complexity 
        # O(n) for the recursion stack