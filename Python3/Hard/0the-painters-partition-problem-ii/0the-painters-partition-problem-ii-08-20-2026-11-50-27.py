class Solution:
    def minTime (self, arr, k):

        def isPossible(maxVal):
            currVal = 0
            currPainter = 1

            for num in arr:
                if currVal + num > maxVal:
                    currPainter += 1
                    currVal = num
                else:
                    currVal += num

            return currPainter <= k

        left = max(arr)
        right = sum(arr)
        ans = 0

        while left <= right:
            mid = left + (right - left) // 2

            if isPossible(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans
