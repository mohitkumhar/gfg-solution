class Solution:
    def findKthSmall(self, arr, k):
        # code here
        arr.sort()

        left = 1
        right = arr[-1] + k

        while left < right:
            mid = left + (right - left) // 2

            missing = mid - self.upperBound(arr, mid)

            if missing < k:
                left = mid + 1
            else:
                right = mid

        return left

    def upperBound(self, arr, target):
        left = 0
        right = len(arr)

        while left < right:
            mid = left + (right - left) // 2

            if arr[mid] <= target:
                left = mid + 1
            else:
                right = mid

        return left
