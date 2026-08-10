class Solution:
    def fourSum(self, arr, target):
        # code here
            
        n = len(arr)
        arr.sort()
        
        result = []
    
        for i in range(n - 3):
            if i > 0 and arr[i] == arr[i - 1]:
                continue
            
            for j in range(i + 1, n - 2):
                if j > i + 1 and arr[j] == arr[j - 1]:
                    continue
    
                low = j + 1
                high = n - 1
    
                while low < high:
                    currSum = arr[i] + arr[j] + arr[low] + arr[high]
    
                    if currSum == target:
                        result.append([arr[i], arr[j], arr[low], arr[high]])
                        
                        while low < high and arr[low] == arr[low + 1]:
                            low += 1
                        while low < high and arr[high] == arr[high - 1]:
                            high -= 1
                        
                        low += 1
                        high -= 1
                    
                    elif currSum < target:
                        low += 1
                    else:
                        high -= 1
            
        return result
