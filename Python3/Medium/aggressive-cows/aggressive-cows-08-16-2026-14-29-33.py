class Solution:
    def aggressiveCows(self, arr, k):

        def isPossible(minDist):

            prevCow = arr[0]
            currCow = 1

            for num in arr:
                currDist = num - prevCow

                if currDist >= minDist:
                    prevCow = num
                    currCow += 1

                if currCow >= k:
                    return True

            return False

        n = len(arr)
        arr.sort()

        left = 0
        # right = arr[n - 1]
        right = arr[n - 1] - arr[0]

        while left <= right:
            mid = left + (right - left) // 2

            if isPossible(mid):
                left = mid + 1
            else:
                right = mid - 1

        return right
