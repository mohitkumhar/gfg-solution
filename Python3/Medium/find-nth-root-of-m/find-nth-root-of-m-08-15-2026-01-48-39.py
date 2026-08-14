class Solution:
    def nthRoot(self, n, m):

        if m == 0:
            return 0
        left = 1
        right = m

        while left <= right:
            mid = left + (right - left) // 2

            currVal = mid ** n

            if currVal == m:
                return mid

            if currVal > m:
                right = mid - 1
            else:
                left = mid + 1

        return - 1
