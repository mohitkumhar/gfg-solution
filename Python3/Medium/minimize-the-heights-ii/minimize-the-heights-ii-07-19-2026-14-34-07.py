class Solution:
    def getMinDiff(self, arr, k):
        arr.sort()
        
        ans = arr[-1] - arr[0]
        
        for i in range(len(arr) - 1):
            if (arr[i + 1] - k) < 0:
                continue

            mini = min(arr[0]  + k, arr[i + 1] - k)
            maxi = max(arr[i] + k, arr[-1] - k)

            ans = min(ans, maxi - mini)
 
        return ans
