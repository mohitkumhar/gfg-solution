class Solution:
    def aggressiveCows(self, arr, k):

        def isPossible(minDist, arr, k):
            currCow = 1
            prevCow = arr[0]

            for num in arr:
                currDist = num - prevCow

                if currDist >= minDist:
                    currCow += 1
                    prevCow = num

                if currCow >= k:
                    return True
            return False


        arr.sort()
        n = len(arr)

        left = 0
        right = arr[n - 1]


        while left <= right:
            mid = left + (right - left) // 2

            if isPossible(mid, arr, k):
                left = mid + 1
            else:
                right = mid - 1

        return right
