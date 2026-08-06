class Solution:
    def medianOf2(self, a, b):
        # code here
        result = []
        nums1 = a
        nums2 = b

        m = len(nums1)
        n = len(nums2)

        i = 0
        j = 0

        while i < m and j < n:
            if nums1[i] < nums2[j]:
                result.append(nums1[i])
                i += 1

            else:
                result.append(nums2[j])
                j += 1

        while i < m:
            result.append(nums1[i])
            i += 1

        while j < n:
            result.append(nums2[j])
            j += 1

        n = len(result)
        if n % 2 == 1:
            return result[n // 2]

        return (result[(n // 2) - 1] + result[n // 2]) / 2
