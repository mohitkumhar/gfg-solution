class Solution:
    def rotateMatrix(self, mat):

        m = len(mat)
        n = len(mat[0])

        for ele in mat:
            ele.reverse()

        for i in range(m):
            for j in range(i + 1, n):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
