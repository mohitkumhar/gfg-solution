class Solution:
    def getSecondLargest(self, arr):
        if len(arr) < 2:
            return -1

        first = -1
        second = -1

        for num in arr:
            if num > first:
                second = first
                first = num
            elif first > num > second:
                second = num

        return second
