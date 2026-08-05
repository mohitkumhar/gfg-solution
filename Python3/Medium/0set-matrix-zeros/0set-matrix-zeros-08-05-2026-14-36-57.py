class Solution:
    def setMatrixZeroes(self, mat):
        m = len(mat)
        n = len(mat[0])
        firstRowZero = False
        firstColZero = False
    
        for i in range(m):
            if mat[i][0] == 0:
                firstColZero = True
                break
    
        for j in range(n):
            if mat[0][j] == 0:
                firstRowZero = True
                break
    
        for i in range(1, m):
            for j in range(1, n):
    
                if mat[i][j] == 0:
                    mat[i][0] = 0
                    mat[0][j] = 0
    
        for i in range(1, m):
            for j in range(1, n):
                if mat[0][j] == 0 or mat[i][0] == 0:
                    mat[i][j] = 0
    
        if firstColZero:
            for i in range(m):
                mat[i][0] = 0
    
        if firstRowZero:
            for j in range(n):
                mat[0][j] = 0
    

            