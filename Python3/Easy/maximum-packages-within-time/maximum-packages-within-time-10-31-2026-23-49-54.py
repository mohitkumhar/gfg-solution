class Solution:
    def maxPackages(self, arr: list[int], totalTime: int) -> int:
        # code here
        n = len(arr)

        windowSum = sum(arr[:totalTime])
        ans = windowSum

        for i in range(totalTime, n):
            windowSum += arr[i]
            windowSum -= arr[i - totalTime]

            ans = max(ans, windowSum)

        return ans