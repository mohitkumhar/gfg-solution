class Solution:
    def cntSubarrays(self, arr, k):
        nums = arr

        count = 0
        n = len(nums)

        prefixTable = {0: 1}
        prefixSum = 0

        for i in range(n):
            prefixSum += nums[i]
            if (prefixSum - k) in prefixTable:
                count += prefixTable[prefixSum - k]

            prefixTable[prefixSum] = prefixTable.get(prefixSum, 0) + 1

        return count
