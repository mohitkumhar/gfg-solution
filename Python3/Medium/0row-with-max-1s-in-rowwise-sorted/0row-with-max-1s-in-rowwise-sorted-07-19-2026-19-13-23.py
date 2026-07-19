class Solution:
    def rowWithMax1s(self, arr):

        n = len(arr)
        max_idx = -1
        j = n - 1

        for i in range(n):

            while j > -1:
                if arr[i][j] == 0:
                    break

                if arr[i][j] == 1:
                    max_idx = i
                    j -= 1

            if j == -1:
                break

        return max_idx
