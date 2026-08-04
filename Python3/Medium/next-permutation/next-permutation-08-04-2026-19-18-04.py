class Solution:
    def nextPermutation(self, arr):
        n = len(arr)
        breakPoint = -1
    
        for i in range(n - 1, 0, -1):
            if arr[i - 1] < arr[i]:
                breakPoint = i - 1
                break
    
        if breakPoint == -1:
            arr.reverse()
            return
    
        for i in range(n - 1, breakPoint - 1, -1):
            if arr[i] > arr[breakPoint]:
                arr[i], arr[breakPoint] = arr[breakPoint], arr[i]
                break
    
        left = breakPoint + 1
        right = n - 1
    
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1


        