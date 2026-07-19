class Solution:
    def rowWithMax1s(self, arr):

        n = len(arr)
        max_one = 0
        max_idx = -1

        for i in range(n):
            for j in range(n - 1, -2, -1):
                if j == -1 or arr[i][j] == 0:
                    total_one = n - j - 1

                    if total_one > max_one:
                        max_one = total_one
                        max_idx = i
                    break

        return max_idx
