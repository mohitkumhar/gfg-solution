class Solution:
    def hasTripletSum(self, arr, target):

        n = len(arr)
        arr.sort()
        result = []

        for k in range(n):
            if k > 0 and arr[k] == arr[k - 1]:  # use to avoid duplicates
                continue
    
            i = k + 1
            j = n - 1
    
            while i < j:
    
                currKey = arr[k] + arr[i] + arr[j]
    
                if currKey == target:
                    result.append([arr[k], arr[i], arr[j]])
    
                    while i < j and arr[i] == arr[i + 1]:  # use to avoid duplicates
                        i += 1
                    while i < j and arr[j] == arr[j - 1]:  # use to avoid duplicates
                        j -= 1
    
                    i += 1
                    j -= 1
    
                elif currKey > target:
                    j -= 1
    
                else:
                    i += 1
    
        return result
    
    
            