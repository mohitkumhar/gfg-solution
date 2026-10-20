from itertools import combinations
class Solution:
    def selectKcities(self, k: int, mat: list[list[int]]) -> int:
        # code here

        n = len(mat)
        ans = float('inf')

        for centers in combinations(range(n), k):
            max_dist = 0

            for city in range(n):
                nearest = min(mat[city][c] for c in centers)
                max_dist = max(max_dist, nearest)

            ans = min(ans, max_dist)

            if ans == 0:
                return 0

        return ans