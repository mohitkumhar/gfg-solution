class Solution:
    def kthSmallest(self, mat, k):

        def find_min_val(val):

            i = n - 1
            j = 0
            count = 0

            while i >= 0 and j < n:
                if mat[i][j] <= val:
                    count += i + 1
                    j += 1
                else:
                    i -= 1

            return count

        n = len(mat)

        left = mat[0][0]
        right = mat[n-1][n-1]

        while left < right:
            mid = left + (right - left) // 2

            count = find_min_val(mid)

            if count >= k:
                right = mid

            else:
                left = mid + 1

        return right
