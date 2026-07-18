class Solution:
    def segregateElements(self, arr):
        i = 0
        j = len(arr) - 1

        pos_ele = []
        neg_ele = []

        for num in arr:
            if num >= 0:
                pos_ele.append(num)
            else:
                neg_ele.append(num)

        arr[:] = pos_ele + neg_ele
