class Solution:
    def inversionCount(self, arr):
        # code here
        

        def merge(left, right, mid, nums):
        
            nums1 = nums[left : mid + 1]
            nums2 = nums[mid + 1: right + 1]
        
            len1 = len(nums1)
            len2 = len(nums2)
        
            i = 0
            j = 0
        
            k = left
            count = 0
        
            while i < len1 and j < len2:
                if nums1[i] > nums2[j]:
                    nums[k] = nums2[j]
                    j += 1
                    count += len1 - i
        
                else:
                    nums[k] = nums1[i]
                    i += 1
                k += 1
        
            while i < len1:
                nums[k] = nums1[i]
                k += 1
                i += 1
        
            while j < len2:
                nums[k] = nums2[j]
                k += 1
                j += 1
            
            return count
        
        def mergeSort(left, right, nums):
            if left >= right:
                return 0
            count = 0
            n = len(nums)
        
            mid = left + (right - left) // 2
        
            count += mergeSort(left, mid, nums)
            count += mergeSort(mid + 1, right, nums)
        
            count += merge(left, right, mid, nums)
        
            return count
        
        return  mergeSort(0, len(arr) - 1, arr)
    

