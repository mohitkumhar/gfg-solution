class Solution:
    def maxGold(self, mat):

        def solve(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or mat[i][j] == 0:
                return 0

            if memo[i][j] != -1 :
                return memo[i][j]

            max_gold = 0

            org_gold = mat[i][j]
            mat[i][j] = 0

            right_up_diag = solve(i - 1, j + 1)
            right = solve(i, j + 1)
            right_down_diag = solve(i + 1, j + 1)

            max_gold = max(max_gold, right_up_diag, right, right_down_diag)

            mat[i][j] = org_gold

            memo[i][j] = mat[i][j] + max_gold
            return memo[i][j]

        m = len(mat)
        n = len(mat[0])

        memo = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]

        max_gold = 0
        for i in range(m):
            if mat[i][0] != 0:
                max_gold = max(max_gold, solve(i, 0))

        return max_gold
