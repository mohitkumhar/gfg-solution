class Solution:
    def kthSmallest(self, arr, k):

        def find_pivot(left, right):
            pivot = arr[left]
            pivot_idx = left

            while left <= right:
                if arr[left] > pivot and arr[right] < pivot:
                    arr[left], arr[right] = arr[right], arr[left]
                    left += 1
                    right -= 1

                if left <= right and arr[left] <= pivot:
                    left += 1

                if left <= right and arr[right] >= pivot:
                    right -= 1

            arr[pivot_idx], arr[right] = arr[right], arr[pivot_idx]

            return right

        left = 0
        right = len(arr) - 1

        while True:
            pivot = find_pivot(left, right)

            if pivot == (k - 1):
                return arr[pivot]

            if pivot > (k-1):
                right = pivot - 1

            if pivot < (k - 1):
                left = pivot + 1
