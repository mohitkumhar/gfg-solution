class Solution:
	def editDistance(self, s1, s2):
		
        def solve(i: int, j: int):
            if i >= n1:
                memo[i][j] = n2 - j
                return n2 - j
            if j >= n2:
                memo[i][j] = n1 - i
                return n1 - i
            if memo[i][j] != -1:
                return memo[i][j]
        
            if s1[i] == s2[j]:
                memo[i][j] = solve(i + 1, j + 1)
                return memo[i][j]
        
            insert = 1 + solve(i, j + 1)
            delete = 1 + solve(i + 1, j)
            replace = 1 + solve(i + 1, j + 1)
        
            memo[i][j] = min(insert, delete, replace)
            return memo[i][j]
        
        n1 = len(s1)
        n2 = len(s2)
        
        memo = [[-1 for _ in range(n2 + 1)] for _ in range(n1 + 1)]
        
        operation = solve(0, 0)
        
        return operation