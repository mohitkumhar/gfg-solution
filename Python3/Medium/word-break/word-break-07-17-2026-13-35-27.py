class Solution:
    def wordBreak(self, s, dictionary):
        dictionary = set(dictionary)

        def solve(i):
            if i == len(s):
                memo[i] = True
                return True
            if memo[i] != -1:
                return memo[i]

            for j in range(i, len(s) + 1):

                if s[i:j] in dictionary and solve(j):
                    memo[i] = True
                    return True
            memo[i] = False
            return False

        memo = [-1] * (len(s) + 1)
        return solve(0)
