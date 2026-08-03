class Solution:
    def longestSubarray(self, arr, k):
        count = 0
        currSum = 0
        prefixSum = {0: -1}

        for i in range(len(arr)):
            currSum += arr[i]

            if (currSum - k) in prefixSum:
                count = max(count, i - prefixSum[currSum - k])
            
            if currSum not in prefixSum:
                prefixSum[currSum] = i

            

        return count
