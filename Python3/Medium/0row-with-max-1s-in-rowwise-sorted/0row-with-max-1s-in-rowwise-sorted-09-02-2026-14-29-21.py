class Solution:
    def rowWithMax1s(self, mat: list[list[int]]) -> int:

        m = len(mat)
        n = len(mat[0])

        i = 0
        j = n - 1

        maxIdx = -1

        for i in range(m):

            while j >= 0:
                if mat[i][j] == 0:
                    break

                if mat[i][j] == 1:
                    maxIdx = i
                    j -= 1

            if j == -1:
                break

        return maxIdx
