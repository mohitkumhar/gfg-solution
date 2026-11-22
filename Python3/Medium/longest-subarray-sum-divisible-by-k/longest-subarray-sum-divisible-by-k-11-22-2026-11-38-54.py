class Solution:
	def longestSubarrayDivK(self, arr, k):
		# code here
        remainderMap = {0: -1}

        prefixSum = 0
        maxLength = 0

        for i in range(len(arr)):
            prefixSum += arr[i]

            remainder = prefixSum % k

            if remainder in remainderMap:
                length = i - remainderMap[remainder]
                maxLength = max(maxLength, length)
            else:
                remainderMap[remainder] = i

        return maxLength
