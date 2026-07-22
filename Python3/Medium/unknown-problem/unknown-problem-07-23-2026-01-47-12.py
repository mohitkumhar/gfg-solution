class Solution:
    def wordBreak(self, s, dictionary):
        dictionary = set(dictionary)
        def solve(i: int) -> bool:
            if i == n:
                return True
            if memo[i] != -1:
                return memo[i]

            for j in range(i, n):
                if s[i : j + 1] in dictionary and solve(j + 1):
                    memo[i] = True
                    return memo[i]
            memo[i] = False
            return memo[i]

        n = len(s)
        memo = [-1] * (n + 1)

        return solve(0)
