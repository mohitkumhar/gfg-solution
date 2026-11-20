class Solution:
    def smallestSubWithSum(self, arr, x):

        n = len(arr)

        i = 0
        currSum = 0
        ans = float('inf')

        for j in range(n):
            currSum += arr[j]

            while currSum > x:
                ans = min(ans, j - i + 1)

                currSum -= arr[i]
                i += 1

        return 0 if ans == float('inf') else ans
