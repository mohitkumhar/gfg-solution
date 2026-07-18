class Solution:
    def sort012(self, arr):

        zeros = 0
        ones = 0
        twos = 0

        for num in arr:
            if num == 0:
                zeros += 1
            elif num == 1:
                ones += 1
            else:
                twos += 1

        arr[:] = [0] * zeros + [1] * ones + [2] * twos
