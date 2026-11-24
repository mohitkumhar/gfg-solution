class Solution:
    def getMinDiff(self, arr, k):
        minVal = float("inf")
        maxVal = float("-inf")

        arr.sort()

        ans = arr[-1] - arr[0]

        for i in range(1, len(arr)):
            if (arr[i] - k) < 0:
                continue

            minVal = min(arr[0] + k, arr[i] - k)
            maxVal = max(arr[-1] - k, arr[i - 1] + k)

            ans = min(ans, maxVal - minVal)

        return ans
