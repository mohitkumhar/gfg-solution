class Solution:
    def maxLength(self, arr):
        n = len(arr)

        prefixSum = {0: -1}
        currSum = 0
        maxLen = 0
    
        for i in range(n):
            currSum += arr[i]
    
            if currSum in prefixSum:
                maxLen = max(maxLen, i - prefixSum[currSum])
    
            else:
                prefixSum[currSum] = i
        
        return maxLen
