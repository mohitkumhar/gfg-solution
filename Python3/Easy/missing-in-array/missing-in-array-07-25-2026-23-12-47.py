class Solution:

    def missingNum(self, arr):
        arr.sort()
        n = len(arr)
        for i in range(1, n + 1):
            if i != arr[i - 1]:
                return i
        return n + 1