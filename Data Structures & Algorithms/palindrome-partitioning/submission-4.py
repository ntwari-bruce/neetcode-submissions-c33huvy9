class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def dfs(remaining, part):
            if not remaining:
                res.append(part.copy())
                return
            for i in range(1, len(remaining) + 1):
                sub = remaining[:i]
                if sub == sub[::-1]:          # palindrome check
                    part.append(sub)
                    dfs(remaining[i:], part)  # pass the rest of the string
                    part.pop()

        dfs(s, [])
        return res

        