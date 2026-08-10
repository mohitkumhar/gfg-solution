class Solution:
    def subarrayXor(self, arr, m):

        n = len(arr)
        prefixXOR = {0: 1}

        currXOR = 0
        count = 0

        for i in range(n):
            currXOR ^= arr[i]

            if currXOR ^ m in prefixXOR:
                count += prefixXOR[currXOR ^ m]

            prefixXOR[currXOR] = prefixXOR.get(currXOR, 0) + 1

        return count
